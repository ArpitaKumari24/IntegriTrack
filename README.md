# 🛡️ File Integrity Checker using SHA256 (Python)

This Python script is designed to **monitor file changes** within a directory and detect if any files have been **modified, deleted, or newly added**. It uses **SHA256 hashing** to ensure data integrity — perfect for tracking sensitive files or ensuring no tampering has occurred.

---

## 🔍 Features

- ✅ Detect **Modified Files**
- 🆕 Detect **Newly Added Files**
- ❌ Detect **Deleted Files**
- 🔐 Uses **SHA256** for strong file hash comparison
- 📝 Simple CLI interface — beginner-friendly!
- 💾 Automatically saves and loads hash records from `hashes.json`

---

## 🚀 How It Works

1. **Initialization**: Generates and stores SHA256 hashes of all files in a folder.
2. **Monitoring**: Compares current file states with the saved hash records.
3. **Report**: Clearly lists modified, new, or deleted files.

---

