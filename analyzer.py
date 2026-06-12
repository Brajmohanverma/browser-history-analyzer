import os
import sqlite3
import shutil
from datetime import datetime, timedelta
from urllib.parse import urlparse

# ─── Config ───────────────────────────────────────────
HISTORY_PATH = os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History"
)
COPY_PATH = "history_copy.db"
TOP_N = 10

# ─── Helper Functions ─────────────────────────────────
def copy_history():
    shutil.copy2(HISTORY_PATH, COPY_PATH)

def get_connection():
    return sqlite3.connect(COPY_PATH)

def convert_time(chrome_time):
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)

def extract_domain(url):
    netloc = urlparse(url).netloc
    netloc = netloc.replace("www.", "")
    # sirf starting ka "m." hatao
    if netloc.startswith("m."):
        netloc = netloc[2:]
    return netloc

# ─── Analysis Functions ───────────────────────────────
def get_top_domains(cursor):
    cursor.execute("SELECT url, visit_count FROM urls;")
    rows = cursor.fetchall()

    domain_counts = {}
    for url, count in rows:
        domain = extract_domain(url)
        if domain:
            domain_counts[domain] = domain_counts.get(domain, 0) + count

    sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_domains[:TOP_N]

def get_peak_hours(cursor):
    cursor.execute("SELECT visit_time FROM visits;")
    rows = cursor.fetchall()

    hour_counts = {}
    for (chrome_time,) in rows:
        hour = convert_time(chrome_time).hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

    return hour_counts

# ─── Report ───────────────────────────────────────────
def print_report(top_domains, hour_counts):
    print("=" * 55)
    print("        🌐 BROWSER HISTORY ANALYZER REPORT")
    print("=" * 55)

    # Top Sites
    print(f"\n📊 Top {TOP_N} Most Visited Domains:\n")
    print(f"  {'Domain':<30} {'Visits':>8}")
    print(f"  {'-'*30} {'-'*8}")
    for domain, count in top_domains:
        print(f"  {domain:<30} {count:>8}")

    # Peak Hours
    print(f"\n⏰ Browsing Activity by Hour:\n")
    peak_hour = max(hour_counts, key=hour_counts.get)
    for hour in sorted(hour_counts.keys()):
        count = hour_counts[hour]
        bar = "█" * (count // 50)
        marker = " ← PEAK" if hour == peak_hour else ""
        print(f"  {hour:02d}:00  {bar} {count}{marker}")

    # Summary
    total_visits = sum(hour_counts.values())
    print(f"\n📈 Summary:")
    print(f"  Total Visits  : {total_visits:,}")
    print(f"  Peak Hour     : {peak_hour:02d}:00 - {peak_hour+1:02d}:00")
    print(f"  Report Date   : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("\n" + "=" * 55)

# ─── Main ─────────────────────────────────────────────
def main():
    copy_history()
    conn = get_connection()
    cursor = conn.cursor()

    top_domains = get_top_domains(cursor)
    hour_counts = get_peak_hours(cursor)

    print_report(top_domains, hour_counts)

    conn.close()

if __name__ == "__main__":
    main()