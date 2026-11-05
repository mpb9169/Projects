import os
import hashlib

# Simulated database of known malware hashes 
KNOWN_MALWARE_HASHES = {
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",  #
    # Add real hashes of known malware here or more of your own for practice
}

def compute_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[!] Could not read file {file_path}: {e}")
        return None

def scan_directory_for_malware(directory):
    print(f"Scanning directory: {directory}")
    infected_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            print(f"Scanning file: {full_path}")
            file_hash = compute_file_hash(full_path)
            if file_hash in KNOWN_MALWARE_HASHES:
                print(f"[INFECTED] {full_path}")
                infected_files.append(full_path)

    if infected_files:
        print("\n Infected files found:")
        for f in infected_files:
            print(f" - {f}")
    else:
        print("\n No known malware found.")


if __name__ == "__main__":
    folder_to_scan = input("Enter folder path to scan: ")
    scan_directory_for_malware(folder_to_scan)


    #Save the script as malware_scanner.py.

#Run it with:

#python malware_scanner.py


#Input the directory you want to scan (e.g., C:\Users\you\Downloads or /home/you/Downloads).

# How to Expand It..



