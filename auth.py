import streamlit as st

# Display login page after lockout
def login_page():
    st.warning("🔒 You have been locked out. Please login to continue.")
    username = st.text_input("Username", key="auth_user")
    password = st.text_input("Password", type="password", key="auth_pass")
    if st.button("Login"):
        # Simple re-login check (demo: username == password)
        if username == password and username:
            st.session_state.lockout = False
            st.session_state.failed_attempts = 0
            st.success("Reauthorized successfully.")
        else:
            st.error("Login failed.")

# Check if user is authenticated
def is_authenticated():
    return not st.session_state.get("lockout", False)

# Lock out user
def logout():
    st.session_state.lockout = True