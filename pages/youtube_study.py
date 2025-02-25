import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def youtube_study_page():
    model = genai.GenerativeModel("gemini-pro")

    def extract_transcript_details(youtube_video_url):
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript

    def generate_gemini_content(transcript_text, prompt):
        response = model.generate_content(prompt + transcript_text)
        return response.text

    st.title("YouTube Transcript to Detailed Notes Converter")
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    submit = st.button("Get Detailed Notes")
    prompt = """You are a YouTube video summarizer. You are provided with various languages like English,
    Hindi, Tamil, Bengali, etc. You will take the transcript text and summarize the entire video,
    providing the important summary in points within 250 words. Provide the summary in English or Hindi."""

    if submit:
        if youtube_link:
            transcript_text = extract_transcript_details(youtube_link)
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)