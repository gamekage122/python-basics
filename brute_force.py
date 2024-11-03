import itertools
import hashlib
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def brute_force_password_cracker(target_hash, charset, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_str = ''.join(guess)
            if hashlib.sha256(guess_str.encode()).hexdigest() == target_hash:
                return f"Password found: {guess_str}"
    return "Password not found"

def main():
    parser = argparse.ArgumentParser(description="Brute Force Password Cracker")
    parser.add_argument("target_hash", help="Target hash to crack")
    parser.add_argument("charset", help="Character set to use for guessing")
    parser.add_argument("max_length", type=int, help="Maximum length of the password")
    
    args = parser.parse_args()
    
    result = brute_force_password_cracker(args.target_hash, args.charset, args.max_length)
    logging.info(result)

if __name__ == "__main__":
    main()
