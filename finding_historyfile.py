import os

# Edge history file ka path
history_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History"
)

# Check karo file exist karti hai ya nahi
if os.path.exists(history_path):
    print("✅ History file mili:", history_path)
else:
    print("❌ File nahi mili")