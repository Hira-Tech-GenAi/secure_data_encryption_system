from cryptography.fernet import Fernet
import base64
import hashlib

# Generate Fernet encryption key using SHA-256 hash
KEY = base64.urlsafe_b64encode(hashlib.sha256(b"my_secret_key").digest())
fernet = Fernet(KEY)

# Encrypt the text data using Fernet
def encrypt_data(data):
    return fernet.encrypt(data.encode()).decode()

# Decrypt the encrypted data
def decrypt_data(token):
    try:
        return fernet.decrypt(token.encode()).decode()
    except:
        return None  # Return None on failure
