import os
import hashlib
import json
import argparse

HASH_FILE = "hashes.json"

def get_file_hash(filepath):
    """Generate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"[!] Error hashing file: {filepath} — {e}")
        return None

def scan_directory(folder_path):
    """Scan all files in a directory and generate hashes."""
    file_hashes = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root, file)
            hash_val = get_file_hash(path)
            if hash_val:
                file_hashes[path] = hash_val
    return file_hashes

def load_hashes():
    """Load saved hash values from file."""
    if not os.path.exists(HASH_FILE):
        return {}
    with open(HASH_FILE, "r") as f:
        return json.load(f)

def save_hashes(hashes):
    """Save hash values to file."""
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def compare_hashes(old, new):
    """Compare old and new hashes and report differences."""
    print("\n🔍 File Integrity Check Report:\n")
    
    modified = []
    deleted = []
    added = []

    for path, old_hash in old.items():
        if path not in new:
            deleted.append(path)
        elif old_hash != new[path]:
            modified.append(path)

    for path in new:
        if path not in old:
            added.append(path)

    if modified:
        print("❗ Modified Files:")
        for file in modified:
            print(f" - {file}")

    if deleted:
        print("\n❌ Deleted Files:")
        for file in deleted:
            print(f" - {file}")

    if added:
        print("\n🆕 New Files:")
        for file in added:
            print(f" - {file}")

    if not modified and not deleted and not added:
        print("✅ No changes detected.")

def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("directory", help="Directory to monitor")
    parser.add_argument("--init", action="store_true", help="Initialize hash records")

    args = parser.parse_args()
    folder_path = args.directory

    if args.init:
        print("[*] Initializing hashes...")
        hashes = scan_directory(folder_path)
        save_hashes(hashes)
        print(f"[✓] Hashes saved for {len(hashes)} files.")
    else:
        print("[*] Checking file integrity...")
        old_hashes = load_hashes()
        new_hashes = scan_directory(folder_path)
        compare_hashes(old_hashes, new_hashes)

if __name__ == "__main__":
    main()
