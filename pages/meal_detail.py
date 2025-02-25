import streamlit as st
import google.generativeai as genai
from PIL import Image
from utils.image_utils import input_image_details
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def meal_detail_page():
    model = genai.GenerativeModel('gemini-1.5-flash')

    def get_gemini_response(input_prompt, image, user_prompt):
        response = model.generate_content([input_prompt, image[0], user_prompt])
        return response.text

    st.header("Meal Details 🍝")
    st.write("Welcome to the Meal Details.")
    st.write("You can ask any questions about the food and I will try to answer it.")
    
    input_text = st.text_input("Enter the query... ", key="input")
    uploaded_file = st.file_uploader("Choose an image of the meal...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me...")
    input_prompt = """
    You are an expert in understanding food items. We will upload an image of various food items, cuisines, dishes
    and you will have to answer any questions based on the uploaded food image. User may ask what is 
    the calorie, fat etc you need to answer it in tabular format. At least you have to detect the food items
    and give a rough idea...
    """

    if submit:
        if uploaded_file:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the meal image")