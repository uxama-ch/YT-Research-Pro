# app.py
import streamlit as st
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth import check_login, logout
from views.keyword_tools import render as keyword_tools_render
from views.optimization_tools import render as optimization_tools_render
from views.planning_tools import render as planning_tools_render
from views.thumbnail_tools import render as thumbnail_tools_render
from views.competitor_tools import render as competitor_tools_render
from views.viral_topics_tool import render as viral_topics_tool_render
import time
from config import API_TIMEOUT, MAX_RETRIES

# Set page config
st.set_page_config(page_title="YouTube Creator Toolkit", layout="wide")

# Authentication
if not check_login():
    st.stop()

# Add logout button in sidebar
st.sidebar.title("📁 Tools Navigation")
if st.sidebar.button("Logout"):
    logout()
    st.stop()

# Add error handling wrapper
def safe_render(render_func):
    try:
        render_func()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please try again or contact support if the issue persists.")

tool = st.sidebar.radio("Select a tool", [
    "Keyword Tools",
    "Optimization Tools",
    "Planning & Scripts",
    "Thumbnail Tools",
    "Competitor Analysis",
    "Viral Topics Tool"
])

# Render selected tool with error handling
if tool == "Keyword Tools":
    safe_render(keyword_tools_render)
elif tool == "Optimization Tools":
    safe_render(optimization_tools_render)
elif tool == "Planning & Scripts":
    safe_render(planning_tools_render)
elif tool == "Thumbnail Tools":
    safe_render(thumbnail_tools_render)
elif tool == "Competitor Analysis":
    safe_render(competitor_tools_render)
elif tool == "Viral Topics Tool":
    safe_render(viral_topics_tool_render)
