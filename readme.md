# 🛡️ Secure Data Encryption System

This is a Streamlit-based secure data storage and retrieval system using Python.

## 🚀 Features
- Encrypt & store data securely using Fernet encryption.
- Users access their own encrypted data with a passkey.
- Incorrect passkey attempts are tracked (3 max).
- Reauthorization via login page after lockout.
- Passkeys hashed with PBKDF2.
- Optional persistent storage using `data.json`.
- Multi-user supported.

## 🖼️ UI Pages
- **Home**: Choose insert or retrieve.
- **Insert Data**: Enter text and passkey to store.
- **Retrieve Data**: Enter username & passkey to decrypt.
- **Login Page**: After 3 failed attempts.

## 📦 Setup Instructions
```bash
pip install streamlit cryptography
streamlit run app.py
```

## 📁 File Structure
```
app.py           # Main Streamlit app
auth.py          # Login page logic
encryption.py    # Encrypt/decrypt functions
storage.py       # Save/load logic
utils.py         # Helper functions (hashing, lockout)
data.json        # Encrypted data storage
README.md        # Project documentation
```

## 📸 Screenshots

### 🔐 Home Page
![Home](screenshots/home.png)

### 📝 Insert Data Page
![Insert Data](screenshots/insert.png)

### 🔍 Retrieve Data Page
![Retrieve Data](screenshots/retrieve.png)

### 🔒 Lockout / Login Page
![Login](screenshots/login.png)

> Save your screenshots in a `screenshots/` folder at the root level and name them accordingly.

---
**Author**: Hira Khalid ✨
