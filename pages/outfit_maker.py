import streamlit as st
import google.generativeai as genai
from PIL import Image
from utils.image_utils import input_image_details
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def outfit_maker_page():
    model = genai.GenerativeModel('gemini-1.5-flash')

    def get_gemini_response(input_prompt, image, prompt):
        response = model.generate_content([input_prompt, image[0], prompt])
        return response.text

    st.header("Outfit Maker 👕")
    input_type = st.radio("Choose the input type", ["Male", "Female", "Kid"])
    input_text = st.text_input("Enter the outfit related query.... ", key="input")
    uploaded_file = st.file_uploader("Choose an image that contains your outfit...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about it....")
    input_prompt = """
    You are an expert in fashion industry where you need to see the outfit from the image and recommend the best suited color of pants with different shirts or footwear or other dress items for men, women, or kids based on the input type.
    You also have to provide the details of every outfit item with the color and brand of the outfit.
    Also you give the score to the outfit based on the color combination and the brand of the outfit out of 10.
    Use may enter the input section and may ask some questions related to outfit then you have to answer all of them.
    Format response as:
    1. Item 1 - color - brand - score - recommended for improvement
    2. Item 2 - color - brand - score - recommended for improvement
    3. Item 3 - color - brand - score - recommended for improvement
    4. Item 4 - color - brand - score - recommended for improvement
    ----
    Overall score of the outfit out of 10 and the best place suited for the clothing (e.g., wedding party, office, casual).
    """

    if submit:
        if uploaded_file:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the image to get the response.")