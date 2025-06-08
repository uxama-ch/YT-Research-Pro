# views/thumbnail_tools.py
import streamlit as st
import pytesseract
from PIL import Image
import openai
from config import OPENAI_API_KEY

def render():
    st.header("🖼️ Thumbnail Tools")
    tool = st.radio("Choose thumbnail tool:", [
        "Thumbnail A/B Tester",
        "Thumbnail Text Extractor"
    ])

    openai.api_key = OPENAI_API_KEY

    if tool == "Thumbnail A/B Tester":
        st.write("Upload two thumbnails to compare")
        img1 = st.file_uploader("Thumbnail A", type=["png", "jpg", "jpeg"], key="1")
        img2 = st.file_uploader("Thumbnail B", type=["png", "jpg", "jpeg"], key="2")

        if img1 and img2 and st.button("Compare Thumbnails"):
            st.image(img1, caption="Thumbnail A", use_column_width=True)
            st.image(img2, caption="Thumbnail B", use_column_width=True)
            st.write("Use audience polls or test click-through rates to pick the best.")

    elif tool == "Thumbnail Text Extractor":
        image_file = st.file_uploader("Upload a thumbnail image", type=["png", "jpg", "jpeg"])
        if image_file:
            image = Image.open(image_file)
            text = pytesseract.image_to_string(image)
            st.subheader("Extracted Text:")
            st.code(text)
