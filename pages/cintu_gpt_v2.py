import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def chintu_gpt_v2_page():
    def get_gemini_response(input_text, image):
        model = genai.GenerativeModel("gemini-1.5-flash")
        if input_text:
            response = model.generate_content([input_text, image])
        else:
            response = model.generate_content(image)
        return response.text
    
    st.header("Chintu GPT V2  📷")
    st.text("Chintu GPT V2 can support image along with text input.")
    st.text("Ask any question in English, Hinglish, German, Telugu-English, etc. and get the answer.")
    
    input_text = st.text_input("Ask the sawal...", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Generate the Jawaab...")

    if submit:
        if input_text and uploaded_file:
            response = get_gemini_response(input_text, image)
            st.subheader("Generated jawaab....")
            st.write(response)
        else:
            st.write("Please enter a question and select an image....")