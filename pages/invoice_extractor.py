import streamlit as st
import google.generativeai as genai
from PIL import Image
from utils.image_utils import input_image_details
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def invoice_extractor_page():
    model = genai.GenerativeModel('gemini-1.5-flash')

    def get_gemini_response(input_prompt, image, user_prompt):
        response = model.generate_content([input_prompt, image[0], user_prompt])
        return response.text

    st.header("Invoice Xtractor  🧊")
    st.write("Welcome to the Invoice Xtractor.")
    st.write("You can ask any questions about the invoice and we will try to answer it.")
    st.write("This model can answer in every language and can read invoice of every language.")
    
    input_text = st.text_input("Enter the query... ", key="input")
    uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about the invoice")
    input_prompt = """
    You are an expert in understanding invoices. We will upload an image as invoice
    and you will have to answer any questions based on the uploaded invoice image
    """

    if submit:
        if uploaded_file:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the invoice image")