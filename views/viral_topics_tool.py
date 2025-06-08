# views/viral_topics_tool.py
import streamlit as st
import openai
import os

def render():
    st.header("🔥 Viral Topics Tool")
    st.write("Use this tool to instantly discover fresh, viral video ideas!")

    openai.api_key = os.getenv("OPENAI_API_KEY")

    if st.button("Start Generating Viral Ideas!"):
        prompt = (
            "Give 5 fresh viral YouTube video ideas. Include:
            - Hook
            - Title
            - Short description (3 lines)
            - Target audience.")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown(response.choices[0].message.content)
