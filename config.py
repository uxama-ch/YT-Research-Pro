# config.py
import streamlit as st

# OpenAI & SERP API Keys
OPENAI_API_KEY = st.secrets["openai"]["api_key"]
SERP_API_KEY = st.secrets.get("serp", {}).get("api_key", "")

# App Configurations
APP_NAME = "YouTube Creator Toolkit"
OWNER_USERNAME = st.secrets["owner"]["username"]
OWNER_PASSWORD = st.secrets["owner"]["password"]

# Other constants
DEFAULT_MIN_VIEW_COUNT = 1000
DEFAULT_SUBSCRIBER_LIMIT = 3000
DEFAULT_TRENDING_DAYS = 5
YOUTUBE_VIDEO_LIMIT = 5

# API Configuration
API_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
RATE_LIMIT_DELAY = 1  # seconds

# File Upload Configuration
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/jpg"]
