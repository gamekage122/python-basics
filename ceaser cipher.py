import argparse

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            result += char
            
    return result

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encoder/Decoder")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("text", help="Text to be encrypted or decrypted")
    parser.add_argument("shift", type=int, help="Shift value (1-25)")
    
    args = parser.parse_args()
    
    if args.shift < 1 or args.shift > 25:
        print("Shift value must be between 1 and 25.")
        return
    
    result = caesar_cipher(args.text, args.shift, args.mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
