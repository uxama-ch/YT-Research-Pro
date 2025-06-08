# utils/auth.py
import streamlit as st
import hashlib
import time
from config import OWNER_USERNAME, OWNER_PASSWORD

# Session timeout in seconds (30 minutes)
SESSION_TIMEOUT = 1800

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login():
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("login_time", 0)

    # Check session timeout
    if st.session_state.logged_in:
        if time.time() - st.session_state.login_time > SESSION_TIMEOUT:
            st.session_state.logged_in = False
            st.session_state.login_time = 0
            st.warning("Session expired. Please login again.")
            return False
        return True

    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == OWNER_USERNAME and hash_password(password) == hash_password(OWNER_PASSWORD):
            st.session_state.logged_in = True
            st.session_state.login_time = time.time()
            st.success("Login successful!")
            st.rerun()
            return True
        else:
            st.error("Invalid credentials.")
    return False

def logout():
    st.session_state.logged_in = False
    st.session_state.login_time = 0
    st.rerun()
