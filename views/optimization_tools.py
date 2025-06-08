# views/optimization_tools.py
import streamlit as st
import openai
import os

def render():
    st.header("📈 Optimization Tools")
    tool = st.radio("Select an optimization task:", [
        "AI Title Generator",
        "SEO Tag Generator",
        "Description Optimizer",
        "YouTube Title Analyzer"
    ])

    openai.api_key = os.getenv("OPENAI_API_KEY")

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

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.write(response.choices[0].message.content)
