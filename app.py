# app.py
import streamlit as st
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth import check_login, logout

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

# Import views dynamically based on selection
if tool == "Keyword Tools":
    from views.keyword_tools import render
    safe_render(render)
elif tool == "Optimization Tools":
    from views.optimization_tools import render
    safe_render(render)
elif tool == "Planning & Scripts":
    from views.planning_tools import render
    safe_render(render)
elif tool == "Thumbnail Tools":
    from views.thumbnail_tools import render
    safe_render(render)
elif tool == "Competitor Analysis":
    from views.competitor_tools import render
    safe_render(render)
elif tool == "Viral Topics Tool":
    from views.viral_topics_tool import render
    safe_render(render)
