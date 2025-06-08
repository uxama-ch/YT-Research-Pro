# views/viral_topics_tool.py
import streamlit as st
from openai import OpenAI
from config import OPENAI_API_KEY

def render():
    st.header("🔥 Viral Topics Tool")
    st.write("Use this tool to instantly discover fresh, viral video ideas!")

    client = OpenAI(api_key=OPENAI_API_KEY)

    if st.button("Start Generating Viral Ideas!"):
        prompt = (
            "Give 5 fresh viral YouTube video ideas. Include:\n"
            "- Hook\n"
            "- Title\n"
            "- Short description (3 lines)\n"
            "- Target audience."
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini-2025-04-14",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error generating ideas: {str(e)}")
