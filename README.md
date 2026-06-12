# 🌐 Browser History Analyzer

A Python CLI tool that analyzes your Microsoft Edge browsing history and generates a detailed report — top visited sites, peak browsing hours, and total activity summary.

---

## 📊 Sample Output

```
=======================================================
        🌐 BROWSER HISTORY ANALYZER REPORT
=======================================================
📊 Top 10 Most Visited Domains:

  Domain                           Visits
  ------------------------------ --------
  youtube.com                        3595
  github.com                         2100
  stackoverflow.com                  1800
  linkedin.com                        590
  ...

⏰ Browsing Activity by Hour:
  18:00  ██████████████████████████ 5527 ← PEAK
  ...

📈 Summary:
  Total Visits  : 42,401
  Peak Hour     : 18:00 - 19:00
=======================================================
```

## 🚀 How to Run

**Requirements:** Python 3.x (no external libraries needed)

**Clone the repo:**
```bash
git clone https://github.com/brajmohanverma/browser-history-analyzer.git
cd browser-history-analyzer
```

**Run the script:**
```bash
python analyzer.py
```

> ⚠️ Currently supports **Microsoft Edge** on Windows only.

---

## 🛠️ How It Works

1. Locates Edge's `History` file (SQLite database)
2. Creates a temporary copy to avoid file lock issues
3. Extracts URLs and visit timestamps
4. Merges duplicate domains (www. and m. variants)
5. Calculates visits per hour from raw timestamps
6. Prints a formatted report in the terminal

---

## 📁 Project Structure
browser-history-analyzer/

├── analyzer.py        # Main script

├── requirements.txt   # No external dependencies

└── README.md          # You are here

---

## 🔮 Planned Features

- [ ] Chrome browser support
- [ ] Last 7 days / 30 days filter
- [ ] Export report to HTML file
- [ ] Matplotlib graphs

---

## 👨‍💻 Author

**Brajmohan**
