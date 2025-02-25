import streamlit as st
import google.generativeai as genai
import json
from utils.pdf_utils import input_pdf_text
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ats_score_check_page():
    def get_gemini_response(input_str):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_str)
        response_dict = json.loads(response.text)
        jd_match = response_dict.get("JD Match", "N/A")
        missing_keywords = response_dict.get("MissingKeywords", [])
        profile_summary = response_dict.get("Profile Summary", "N/A")
        return f"JD Match: {jd_match}\nMissing Keywords: {missing_keywords}\nProfile Summary: {profile_summary}"

    st.title("Gen ATS")
    st.text("Improve Your Resume ATS score")
    
    jd = st.text_area("Paste the Job Description...")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            resume_text = input_pdf_text(uploaded_file)
            input_str = """
                Hey Act Like a skilled or very experienced ATS (Application Tracking System)
                with a deep understanding of the tech field, software engineering, data science, data analysis,
                and big data engineering. Your task is to evaluate the resume based on the given job description.
                You must consider the job market is very competitive and you should provide the
                best assistance for improving the resumes. Assign the percentage Matching based 
                on JD and the missing keywords with high accuracy.
                resume:{text}
                description:{jd}
                I want the response in one single string having the structure
                {{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
            """.format(text=resume_text, jd=jd)
            response = get_gemini_response(input_str)
            st.subheader("ATS Score and Insights:")
            st.text(response)
        else:
            st.error("Please upload a resume PDF file.")