import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def image_to_code_page():
    model = genai.GenerativeModel("gemini-1.5-flash")

    def get_code_from_image(image, code_type):
        if code_type == "HTML/CSS/JavaScript/React":
            prompt = "Generate a responsive webpage code (HTML, CSS, JavaScript, React) based on the contents of this image."
        elif code_type == "Kotlin":
            prompt = "Generate a Kotlin application based on the contents of this image."
        response = model.generate_content([prompt, image])
        return response.text
    
    st.header("Image-to-Code Generator 🖼️➡️💻")
    st.text("Upload an image and receive code in your chosen language or framework.")

    uploaded_file = st.file_uploader("Upload an image (jpg, png, etc.)", type=["jpg", "jpeg", "png"])
    code_type = st.selectbox("Select the type of code to generate:", ("HTML/CSS/JavaScript/React", "Kotlin"))

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        submit = st.button("Generate Code")
        if submit:
            code_response = get_code_from_image(image, code_type)
            st.subheader(f"Generated {code_type} Code")
            st.code(code_response, language="html" if code_type == "HTML/CSS/JavaScript/React" else "kotlin")
    else:
        st.write("Please upload an image to generate code.")