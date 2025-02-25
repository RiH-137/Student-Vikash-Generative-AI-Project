import streamlit as st
import google.generativeai as genai
from PIL import Image
from utils.image_utils import input_image_details
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def aesthetic_rating_page():
    model = genai.GenerativeModel('gemini-1.5-flash')

    def get_gemini_response(input_prompt, image, prompt):
        response = model.generate_content([input_prompt, image[0], prompt])
        return response.text

    st.header("Aesthetic Rating 🦸‍♀️")
    input_type = st.radio("Choose the input type", ["Male", "Female", "Kid"])
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about it....")
    input_prompt = """
    You are an expert in fashion industry and Instagram influence where you need to see the outfit, model pose, background, aestheticness from the image and recommend the best pose with different outfits and backgrounds.
    Provide different poses, backgrounds, filters, camera angles, and dresses for the model image.
    Format response as:
    pose - background of the image - filter - environment - outfit - style - aestheticness score (1-10) - good for social media (Yes/No, percentage).
    ----
    At the end, suggest how the model can improve their photoshoot image (e.g., wedding party, office, casual) in tabular format.
    """

    if submit:
        if uploaded_file:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input_type)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the image to get the response.")