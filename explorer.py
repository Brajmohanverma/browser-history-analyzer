import os
import sqlite3

# Edge history file ka path
history_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History"
)

# File copy karke read karenge (Edge ne lock rakhi hoti hai original)
import shutil
shutil.copy2(history_path, "history_copy.db")

# Database open karo
conn = sqlite3.connect("history_copy.db")
cursor = conn.cursor()

# Saari tables dekho
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in History database:")
for table in tables:
    print(" -", table[0])

conn.close()