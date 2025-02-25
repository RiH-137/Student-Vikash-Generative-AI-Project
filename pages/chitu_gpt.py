import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def chintu_gpt_page():
    def get_gemini_response(input_text):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(input_text)
        return response.text

    if 'history' not in st.session_state:
        st.session_state.history = []

    st.header("Chintu GPT V1 - Chatbot")
    st.text("Ask questions in any language (English, Hinglish, German, Telugu-English) and get answers.")
    
    input_text = st.text_input("Talk to me...", key="input")
    submit = st.button("Generate the reply...")

    if submit:
        if input_text:
            response = get_gemini_response(input_text)
            st.session_state.history.append({"input": input_text, "response": response})
            st.subheader("Conversation History:")
            for idx, chat in enumerate(st.session_state.history):
                st.write(f"**Q{idx + 1}:** {chat['input']}")
                st.write(f"**A{idx + 1}:** {chat['response']}")
                st.text("---")
        else:
            st.write("Please enter a question to get a response.")