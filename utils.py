import streamlit as st
from hashlib import pbkdf2_hmac

# Initialize session state variables
def init_session_state():
    if "failed_attempts" not in st.session_state:
        st.session_state.failed_attempts = 0
    if "lockout" not in st.session_state:
        st.session_state.lockout = False
    if "data_store" not in st.session_state:
        st.session_state.data_store = {}

# Check if user exceeded allowed attempts
def lockout_check():
    if st.session_state.failed_attempts >= 3:
        st.session_state.lockout = True
        return True
    return False

# Reset failed attempt count
def reset_attempts():
    st.session_state.failed_attempts = 0

# Hash the passkey using PBKDF2 for better security
def hash_passkey(passkey):
    salt = b"my_salt"
    hashed = pbkdf2_hmac('sha256', passkey.encode(), salt, 100000)
    return hashed.hex()
