def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        elif 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift)

def decrypt(text, shift):
    return caesar_cipher(text, -shift)

def brute_force_attack(ciphertext):
    print("\n========== BRUTE FORCE RESULTS ==========")
    for shift in range(1, 26):
        possible_text = decrypt(ciphertext, shift)
        print(f"Shift {shift:2d}: {possible_text}")

def main():
    while True:
        print("\n======================================")
        print("        ADVANCED CAESAR CIPHER")
        print("======================================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Exit")
        print("======================================")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            plaintext = input("\nEnter plaintext: ")
            try:
                shift = int(input("Enter shift value: "))
                ciphertext = encrypt(plaintext, shift)
                print("\n----- ENCRYPTION -----")
                print("Ciphertext:", ciphertext)
            except ValueError:
                print("Invalid shift! Please enter an integer.")
                
        elif choice == "2":
            ciphertext = input("\nEnter ciphertext: ")
            try:
                shift = int(input("Enter shift value: "))
                plaintext = decrypt(ciphertext, shift)
                print("\n----- DECRYPTION -----")
                print("Plaintext:", plaintext)
            except ValueError:
                print("Invalid shift! Please enter an integer.")
                
        elif choice == "3":
            ciphertext = input("\nEnter ciphertext: ")
            brute_force_attack(ciphertext)
            
        elif choice == "4":
            print("\nProgram terminated.")
            break
        else:
            print("\nInvalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()