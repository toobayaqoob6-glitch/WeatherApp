# Install the cryptography library in colab
!pip install cryptography

# Import the Fernet class from cryptography
from cryptography.fernet import Fernet

# Step 1: Generate a secret key
key = Fernet.generate_key()

# decode() turns the bytes key into a clean string for printing
print("Generated Key:", key.decode())

# Step 2: Create a Fernet object with the key
cipher = Fernet(key)

# Step 3: Define the message you want to encrypt
message = "tooba yaqoob is a student of dawood university."
print("\nOriginal Message:", message)

# Step 4: Convert the message into bytes
message_bytes = message.encode()

# Step 5: Encrypt the message using the Fernet cipher
encrypted_message = cipher.encrypt(message_bytes)

# decode() lets you see the token clearly without the b'' prefix
print("\nEncrypted Message:", encrypted_message.decode())

# Step 6: Decrypt the encrypted message back to plain text
decrypted_message = cipher.decrypt(encrypted_message)
print("\nDecrypted Message:", decrypted_message.decode())
