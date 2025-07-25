# views/planning_tools.py
import streamlit as st
from openai import OpenAI
from config import OPENAI_API_KEY

def render():
    st.header("📅 Planning & Scripts")
    tool = st.radio("Select a planning tool:", [
        "Content Calendar with AI Suggestions",
        "Script Hook Generator",
        "Content Gap Analyzer"
    ])

    client = OpenAI(api_key=OPENAI_API_KEY)

    topic = st.text_input("Enter your channel or topic:")
    if topic and st.button("Generate"):
        if tool == "Content Calendar with AI Suggestions":
            prompt = f"Create a 2-week YouTube content calendar for the channel/topic: {topic}"
        elif tool == "Script Hook Generator":
            prompt = f"Write 5 attention-grabbing YouTube script hooks for videos on: {topic}"
        elif tool == "Content Gap Analyzer":
            prompt = f"Analyze potential content gaps for a YouTube channel focused on: {topic}"

        response = client.chat.completions.create(
            model="gpt-4.1-mini-2025-04-14",
            messages=[{"role": "user", "content": prompt}]
        )
        st.write(response.choices[0].message.content)
