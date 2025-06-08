# views/viral_topics_tool.py
import streamlit as st
import openai
from config import OPENAI_API_KEY

def render():
    st.header("🔥 Viral Topics Tool")
    st.write("Use this tool to instantly discover fresh, viral video ideas!")

    openai.api_key = OPENAI_API_KEY

    if st.button("Start Generating Viral Ideas!"):
        prompt = (
            "Give 5 fresh viral YouTube video ideas. Include:\n"
            "- Hook\n"
            "- Title\n"
            "- Short description (3 lines)\n"
            "- Target audience."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error generating ideas: {str(e)}")
