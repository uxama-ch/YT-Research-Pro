# views/keyword_tools.py
import streamlit as st
from openai import OpenAI
import requests
from config import OPENAI_API_KEY, SERP_API_KEY

def render():
    st.header("🔑 Keyword Tools")
    tool = st.radio("Choose a keyword tool:", [
        "Keyword Suggestion Tool",
        "Long-Tail Keyword Explorer",
        "Trending Topic Finder by Niche"
    ])

    client = OpenAI(api_key=OPENAI_API_KEY)

    if tool == "Keyword Suggestion Tool":
        keyword = st.text_input("Enter a topic:")
        if keyword and st.button("Suggest Keywords"):
            prompt = f"Suggest SEO keywords related to the topic: {keyword}"
            response = client.chat.completions.create(
                model="gpt-4.1-mini-2025-04-14",
                messages=[{"role": "user", "content": prompt}]
            )
            st.write(response.choices[0].message.content)

    elif tool == "Long-Tail Keyword Explorer":
        base_keyword = st.text_input("Base Keyword:")
        if base_keyword and st.button("Generate Long-Tail Keywords"):
            prompt = f"Generate long-tail keyword variations for: {base_keyword}"
            response = client.chat.completions.create(
                model="gpt-4.1-mini-2025-04-14",
                messages=[{"role": "user", "content": prompt}]
            )
            st.write(response.choices[0].message.content)

    elif tool == "Trending Topic Finder by Niche":
        niche = st.text_input("Enter your niche (e.g. tech, beauty, etc):")
        if niche and st.button("Find Trending Topics"):
            url = f"https://serpapi.com/search.json?q={niche}+trending&tbm=nws&api_key={SERP_API_KEY}"
            res = requests.get(url).json()
            for article in res.get("news_results", [])[:5]:
                st.subheader(article.get("title"))
                st.write(article.get("link"))
                st.caption(article.get("snippet"))
