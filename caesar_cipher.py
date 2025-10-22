def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  
    return result


def main():
    print("=== Caesar Cipher Encryption & Decryption ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please type 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"\nYour {mode}ed message: {result}")


if __name__ == "__main__":
    main()
