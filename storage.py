import json
import streamlit as st
from encryption import decrypt_data
from utils import hash_passkey

DATA_FILE = "data.json"  # File to store data persistently

# Load encrypted data from JSON into session state
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            st.session_state.data_store = json.load(f)
    except:
        st.session_state.data_store = {}

# Save current session state data to JSON
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(st.session_state.data_store, f)

# Store new data for a user
def store_data(username, encrypted_text, passkey):
    user_data = {
        "encrypted_text": encrypted_text,
        "passkey": hash_passkey(passkey)
    }
    st.session_state.data_store[username] = user_data

# Retrieve and decrypt data if passkey is valid
def retrieve_data(username, passkey):
    data = st.session_state.data_store.get(username)
    if data and hash_passkey(passkey) == data["passkey"]:
        return decrypt_data(data["encrypted_text"])
    return None