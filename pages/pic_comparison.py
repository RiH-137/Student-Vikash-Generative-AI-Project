import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def pic_comparison():
    model = genai.GenerativeModel('gemini-1.5-flash')

    def get_gemini_response(input_prompt, image_data, caption_prompt="", hashtag_prompt=""):
        combined_prompt = input_prompt + caption_prompt + hashtag_prompt
        response = model.generate_content([combined_prompt] + image_data)
        return response.text

    st.header("Which picture is best for Instagram?")
    uploaded_file1 = st.file_uploader("Choose the first image...", type=["jpg", "jpeg", "png"])
    uploaded_file2 = st.file_uploader("Choose the second image...", type=["jpg", "jpeg", "png"])

    if uploaded_file1:
        image1 = Image.open(uploaded_file1)
        st.image(image1, caption="First Uploaded Image", use_column_width=True)
    if uploaded_file2:
        image2 = Image.open(uploaded_file2)
        st.image(image2, caption="Second Uploaded Image", use_column_width=True)

    submit = st.button("Compare Pictures")
    input_prompt = """ You are an expert in the fashion industry and you are a great fashion influence. You have been given two images as input and you have to 
    give a description of both the images and you have to tell which image is best and why for the Instagram post with the 
    good caption and the best suited hashtags."""

    if submit:
        if uploaded_file1 and uploaded_file2:
            image_data = [image1, image2]
            caption_prompt = "\nHere are some caption ideas for the image:"
            hashtag_prompt = "\nHere are some hashtag suggestions for the image:"
            response = get_gemini_response(input_prompt, image_data, caption_prompt, hashtag_prompt)
            st.subheader("GenAI Response:")
            st.write(response)