import streamlit as st
from auth import login_page, is_authenticated, logout
from encryption import encrypt_data, decrypt_data
from storage import store_data, retrieve_data, load_data, save_data
from utils import init_session_state, lockout_check, reset_attempts

# Configure Streamlit page
st.set_page_config(page_title="🔐 Secure Data Encryption System", layout="centered")

# Initialize session state and load data from JSON
init_session_state()
load_data()

# If locked out, show login page
if st.session_state.get("lockout"):
    login_page()
    st.stop()

# Home page UI
st.title("🔐 Secure Data Encryption System")
st.markdown("Choose an action below:")

# Navigation options
option = st.radio("Select", ["Insert Data", "Retrieve Data", "Logout"])

if option == "Insert Data":
    # UI for inserting data
    st.subheader("📝 Insert Secure Data")
    username = st.text_input("Username")
    text = st.text_area("Enter text")
    passkey = st.text_input("Passkey", type="password")
    if st.button("Encrypt & Store"):
        if username and text and passkey:
            encrypted = encrypt_data(text)
            store_data(username, encrypted, passkey)
            st.success("Data securely stored.")
            save_data()  # Save to JSON file
        else:
            st.error("All fields are required.")

elif option == "Retrieve Data":
    # UI for retrieving data
    st.subheader("🔍 Retrieve Data")
    username = st.text_input("Username")
    passkey = st.text_input("Enter your passkey", type="password")
    if st.button("Decrypt"):
        if username and passkey:
            if lockout_check():
                st.error("Too many failed attempts. Please login again.")
            else:
                decrypted = retrieve_data(username, passkey)
                if decrypted:
                    st.success("Here is your decrypted data:")
                    st.code(decrypted)
                    reset_attempts()  # Reset failed attempts
                else:
                    st.error("Invalid credentials.")
                    st.session_state.failed_attempts += 1
        else:
            st.error("All fields are required.")

elif option == "Logout":
    # Logout functionality
    logout()
    st.success("Logged out successfully.")
