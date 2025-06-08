# views/optimization_tools.py
import streamlit as st
from openai import OpenAI
from config import OPENAI_API_KEY

def render():
    st.header("📈 Optimization Tools")
    tool = st.radio("Select an optimization task:", [
        "AI Title Generator",
        "SEO Tag Generator",
        "Description Optimizer",
        "YouTube Title Analyzer"
    ])

    client = OpenAI(api_key=OPENAI_API_KEY)

    input_text = st.text_area("Enter content:")
    if input_text and st.button("Run Tool"):
        if tool == "AI Title Generator":
            prompt = f"Generate 5 catchy YouTube video titles for: {input_text}"
        elif tool == "SEO Tag Generator":
            prompt = f"Suggest SEO tags for a YouTube video about: {input_text}"
        elif tool == "Description Optimizer":
            prompt = f"Write an SEO-optimized YouTube video description for: {input_text}"
        elif tool == "YouTube Title Analyzer":
            prompt = f"Analyze and rate this YouTube title for SEO and engagement: {input_text}"

        response = client.chat.completions.create(
            model="gpt-4.1-mini-2025-04-14",
            messages=[{"role": "user", "content": prompt}]
        )
        st.write(response.choices[0].message.content)
