import streamlit as st
import google.generativeai as genai
from PIL import Image
from utils.image_utils import input_image_details
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def img_to_text():
    model = genai.GenerativeModel('gemini-1.5-flash')

    def get_gemini_response(input_prompt, image, prompt):
        response = model.generate_content([input_prompt, image[0], prompt])
        return response.text

    st.header("Image to Text Converter 📷")
    input_text = st.text_input("Enter any query.... ", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Convert it into text....")
    input_prompt = """
    Here user may upload handwritten or computer typed text image and you have to convert the text from the image to the text.
    and you have to provide the details of the text in the form of the text.
    and you have to return the text in the form of the text... and you have display the whole text first and 
    then convert and translate the text into hindi language.
    """

    if submit:
        if uploaded_file:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the image to get the response, as the image is not uploaded.")