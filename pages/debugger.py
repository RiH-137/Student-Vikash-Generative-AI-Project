import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def debugger_page():
    def get_debugger_response(code, error):
        model = genai.GenerativeModel("gemini-1.5-flash")
        if code and error:
            prompt = f"Here is the code: \n{code}\nAnd here is the error:\n{error}\nPlease provide debugging suggestions."
        elif code:
            prompt = f"Here is the code: \n{code}\nPlease identify any potential issues or improvements."
        else:
            prompt = f"Here is the error: \n{error}\nPlease provide suggestions on how to fix it."
        response = model.generate_content([prompt])
        return response.text
    
    st.header("Code Debugger 🐞")
    st.text("Paste your code and error below to get debugging help.")

    code_input = st.text_area("Paste the code here...", height=200)
    error_input = st.text_area("Paste the error message here...", height=100)
    submit = st.button("Debug")

    if submit:
        if code_input or error_input:
            response = get_debugger_response(code_input, error_input)
            st.subheader("Debugger Output")
            st.write(response)
        else:
            st.write("Please provide either code or an error message to proceed.")