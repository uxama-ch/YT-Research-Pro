# views/competitor_tools.py
import streamlit as st
import requests
from config import SERP_API_KEY

def render():
    st.header("🔎 Competitor Analysis")
    tool = st.radio("Select competitor tool:", [
        "Competitor Channel Tracker",
        "Public Video Stats Tracker"
    ])

    if tool == "Competitor Channel Tracker":
        channel = st.text_input("Enter competitor's channel name:")
        if channel and st.button("Search Channel"):
            query = f"site:youtube.com {channel}"
            url = f"https://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}"
            res = requests.get(url).json()
            for r in res.get("organic_results", [])[:3]:
                st.subheader(r.get("title"))
                st.write(r.get("link"))

    elif tool == "Public Video Stats Tracker":
        keyword = st.text_input("Search by video topic or title:")
        if keyword and st.button("Find Videos"):
            url = f"https://serpapi.com/search.json?q={keyword}+site:youtube.com&api_key={SERP_API_KEY}"
            res = requests.get(url).json()
            for result in res.get("video_results", [])[:5]:
                st.subheader(result.get("title"))
                st.write(result.get("link"))
                st.caption(result.get("published_date", ""))
