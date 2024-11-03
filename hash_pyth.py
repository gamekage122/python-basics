import os
import hashlib
import argparse
import logging
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_sha256(file_path):
    """Generate SHA-256 hash for a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in tqdm(iter(lambda: f.read(4096), b""), desc=f"Processing {file_path}", unit="B", unit_scale=True):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
        return None

def check_integrity(file_paths):
    """Check integrity of files by generating their SHA-256 hashes."""
    for file_path in file_paths:
        if os.path.isfile(file_path):
            hash_value = generate_sha256(file_path)
            if hash_value:
                logging.info(f"{file_path}: {hash_value}")
        else:
            logging.warning(f"{file_path} does not exist.")

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Check file integrity by generating SHA-256 hashes.")
    parser.add_argument("files", metavar="F", type=str, nargs="+", help="Files to check")
    args = parser.parse_args()

    check_integrity(args.files)
