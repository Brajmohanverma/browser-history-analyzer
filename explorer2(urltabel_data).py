import os
import sqlite3
import shutil

history_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History"
)

shutil.copy2(history_path, "history_copy.db")

conn = sqlite3.connect("history_copy.db")
cursor = conn.cursor()

# urls table ke columns dekho
cursor.execute("PRAGMA table_info(urls);")
columns = cursor.fetchall()

print("Columns in urls table:")
for col in columns:
    print(" -", col[1])

conn.close()