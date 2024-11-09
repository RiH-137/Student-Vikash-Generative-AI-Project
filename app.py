from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader
from youtube_transcript_api import YouTubeTranscriptApi
import os
import google.generativeai as genai
import json
import textwrap
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
# from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

import PyPDF2 as pdf
from dotenv import load_dotenv
import json




# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#========================================================================================================



def chintu_gpt_page():
    # Function to get response from Gemini model
    def get_gemini_response(input_text):
        # Update the model to the new version "gemini-1.5-flash"
        model2 = genai.GenerativeModel("gemini-1.5-flash")
        
        # Send the input text to the model for generating the response
        response = model2.generate_content(input_text)
        return response.text

    # Initialize session state to store conversation history if not already present
    if 'history' not in st.session_state:
        st.session_state.history = []

    st.header("Chintu GPT V2 - Chatbot")
    st.text("Ask questions in any language (English, Hinglish, German, Telugu-English) and get answers.")
    
    # Input area for user question
    input_text = st.text_input("Talk to me...", key="input")
    
    # Button to submit the question
    submit = st.button("Generate the reply...")

    if submit:
        if input_text:  # Ensure that the user has entered a question
            response = get_gemini_response(input_text)
            
            # Store the conversation history
            st.session_state.history.append({"input": input_text, "response": response})

            # Display the entire conversation history
            st.subheader("Conversation History:")
            for idx, chat in enumerate(st.session_state.history):
                st.write(f"**Q{idx + 1}:** {chat['input']}")
                st.write(f"**A{idx + 1}:** {chat['response']}")
                st.text("---")  # Separator for clarity

        else:
            st.write("Please enter a question to get a response.")




#========================================================================================================
# Page: Chintu GPT V2
import streamlit as st
from PIL import Image
import google.generativeai as genai

def chintu_gpt_v2_page():
    def get_gemini_response(input, image):
        # Update the model to the new version "gemini-1.5-flash"
        model2 = genai.GenerativeModel("gemini-1.5-flash")
        if input != "":
            response = model2.generate_content([input, image])
        else:
            response = model2.generate_content(image)
        return response.text
    
    st.header("Chintu GPT V2  📷")
    st.text("Chintu GPT V2 can support image along with text input.")
    st.text(" Ask any question in English, Hinglish, German, Telugu-English, etc. and get the answer.")
    
    input = st.text_input("Ask the sawal...", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    image = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Generate the Jawaab...")

    if submit:
        if input and image:
            response = get_gemini_response(input, image)
            st.subheader("Generated jawaab....")
            st.write(response)
        else:
            st.write("Please enter a question and select an image....")
#======================================================================================================================

## debugger
import streamlit as st
import google.generativeai as genai

def debugger_page():
    # Function to process the code and error and generate a response
    def get_debugger_response(code, error):
        # Update the model to a version like "gemini-1.5-flash" or another generative AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        if code and error:
            prompt = f"Here is the code: \n{code}\nAnd here is the error:\n{error}\nPlease provide debugging suggestions."
        elif code:
            prompt = f"Here is the code: \n{code}\nPlease identify any potential issues or improvements."
        else:
            prompt = f"Here is the error: \n{error}\nPlease provide suggestions on how to fix it."
        
        # Generate the response based on the prompt
        response = model.generate_content([prompt])
        return response.text
    
    st.header("Code Debugger 🐞")
    st.text("Paste your code and error below to get debugging help.")

    # Input box for the code
    code_input = st.text_area("Paste the code here...", height=200)

    # Input box for the error message
    error_input = st.text_area("Paste the error message here...", height=100)

    # Submit button to trigger the debug process
    submit = st.button("Debug")

    # Handle the debug request when submit is clicked
    if submit:
        if code_input or error_input:
            response = get_debugger_response(code_input, error_input)
            st.subheader("Debugger Output")
            st.write(response)
        else:
            st.write("Please provide either code or an error message to proceed.")

#=================`=======================================================================================================
## PDF se padhai

import streamlit as st
import json

from PyPDF2 import PdfReader

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Function to get response from Gemini API
def get_gemini_response(input):
    model5 = genai.GenerativeModel('gemini-pro')
    response = model5.generate_content(input)
    response_dict = json.loads(response.text)

    # Extract JD Match percentage, missing keywords, and profile summary
    jd_match = response_dict.get("JD Match", "N/A")
    missing_keywords = response_dict.get("MissingKeywords", [])
    profile_summary = response_dict.get("Profile Summary", "N/A")

    # Create a formatted response string
    formatted_response = f"JD Match: {jd_match}\nMissing Keywords: {missing_keywords}\nProfile Summary: {profile_summary}"
    return formatted_response

# Function to answer questions based on the resume
def get_answer_to_question(text, question):
    input_str = f"Answer the following question based on the text:\n\n{text}\n\nQuestion: {question}\nAnswer:"
    model5 = genai.GenerativeModel('gemini-pro')
    response = model5.generate_content(input_str)
    response_dict = json.loads(response.text)
    return response_dict.get('Answer', 'Sorry, I cannot answer this question.')

# Streamlit app
def ats_score_check_page():
    st.title("Gen ATS")
    st.text("Improve Your Resume ATS score")
    
    # Input fields for Job Description and Resume PDF
    jd = st.text_area("Paste the Job Description...")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

    # Submit button
    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            # Extract text from PDF
            resume_text = input_pdf_text(uploaded_file)

            # Generate ATS score and other information
            input_str = """
                Hey Act Like a skilled or very experienced ATS (Application Tracking System)
                with a deep understanding of the tech field, software engineering, data science, data analysis,
                and big data engineering. Your task is to evaluate the resume based on the given job description.
                You must consider the job market is very competitive and you should provide the
                best assistance for improving the resumes. Assign the percentage Matching based 
                on JD and
                the missing keywords with high accuracy.
                resume:{text}
                description:{jd}

                I want the response in one single string having the structure
                {{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
            """
            input_str = input_str.format(text=resume_text, jd=jd)
            response = get_gemini_response(input_str)
            st.subheader("ATS Score and Insights:")
            st.text(response)

            # Question and Answer Section
            question = st.text_input("Ask a question about the resume or job description:")
            if question:
                answer = get_answer_to_question(resume_text, question)
                st.subheader("Answer:")
                st.text(answer)
        else:
            st.error("Please upload a resume PDF file.")




#===========================================================================================================================
# Page: Invoice Extractor
def invoice_extractor_page():

    model3=genai.GenerativeModel('gemini-1.5-flash')

   #image means the image of the invoice  #user_prompt means the question asked by the user
    def get_gemini_response(input,image,user_prompt):  
        response=model3.generate_content([input,image[0],user_prompt])
        return response.text



    #conversion of image data into bytes
    def input_image_details(uploaded_file):
        if uploaded_file is not None:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()

            image_parts = [
                {
                    "mime_type": uploaded_file.type,  # get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")
        
    st.header("Invoice Xtractor  🧊")
    st.write("Welcome to the Invoice Xtractor.")
    st.write("You can ask any questions about the invoice and we will try to answer it.")
    st.write("This model can answer in every language and can read invoice of every language.")
    input=st.text_input("Enter the query... ",key="input")
    uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image=Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit=st.button("Tell me about the invoice")

    input_prompt="""
    You are an expert in understanding invoices. We will upload a a image as invoice
    and you will have to answer any questions based on the uploaded invoice image
    """

    ## if submit button is clicked

    if submit:
        if uploaded_file:
            image_data=input_image_details(uploaded_file)
            response=get_gemini_response(input_prompt,image_data,input)
            st.subheader("The Rresponse is")
            st.write(response)
        else:
            st.error("Please upload the invoice image")

#====  ======================================================================================================================
def img_to_text():

    def get_gemini_repsonse(input,image,prompt):
        model12=genai.GenerativeModel('gemini-1.5-flash')
        response=model12.generate_content([input,image[0],prompt])
        return response.text




    #conversion of image data to bytes
    def input_image_for_text(uploaded_file):
        # Check if a file has been uploaded
        if uploaded_file is not None:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()  # Read the file into bytes

            image_parts = [
                {
                    "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")
        

    st.header("Image to Text Converter 📷")
    input=st.text_input("Enter any query.... ",key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)


    submit=st.button("Convert it into text....")

    input_prompt="""
    Here use may upload handwritten or computer typed text image and you have to convert the text from the image to the text.
    and you have to provide the details of the text in the form of the text.
    and you have to return the text in the form of the text... and you have display the whole text first and 
    then convert and translate the text into hindi language.
                ----
                ----


    """

    ## If submit button is clicked

    if submit:
        if uploaded_file:
            image_data=input_image_for_text(uploaded_file)
            response=get_gemini_repsonse(input_prompt,image_data,input)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the image to get the response, as the image is not uploaded.")
#=====================================================================================================================
def pic_comparison():

    def get_gemini_response(input_prompt, image_data, caption_prompt="", hashtag_prompt=""):
        """
        Calls the GenAI model to analyze images and generate recommendations.

        Args:
            input_prompt: String containing the initial prompt for GenAI.
            image_data: List containing two PIL Image objects.
            caption_prompt: Optional string prompt for generating captions (default "").
            hashtag_prompt: Optional string prompt for generating hashtags (default "").

        Returns:
            String containing the GenAI response, including analysis and recommendations.
        """

        model5 = genai.GenerativeModel('gemini-1.5-flash')
        combined_prompt = input_prompt + caption_prompt + hashtag_prompt
        response = model5.generate_content([combined_prompt] + image_data)
        return response.text

    st.header("Which picture is best for Instagram?")

    uploaded_file1 = st.file_uploader("Choose the first image...", type=["jpg", "jpeg", "png"])
    image1 = None
    if uploaded_file1 is not None:
        image1 = Image.open(uploaded_file1)
        st.image(image1, caption="First Uploaded Image", use_column_width=True)

    uploaded_file2 = st.file_uploader("Choose the second image...", type=["jpg", "jpeg", "png"])
    image2 = None
    if uploaded_file2 is not None:
        image2 = Image.open(uploaded_file2)
        st.image(image2, caption="Second Uploaded Image", use_column_width=True)
    input_prompt = """ You are an expert in the fashion industry and you are a great fashion influence. You have been given two images as input and you have to 
  give a description of both the images and you have to tell which image is best and why for the Instagram post with the 
  good caption and the best suited hashtags."""
    submit_button = st.button("Compare Pictures")

    if submit_button:
        if uploaded_file1 and uploaded_file2:
            image_data = [image1, image2]

            # Separate prompts for better control over caption & hashtag generation
            caption_prompt = """
                Here are some caption ideas for the image:
            """
            hashtag_prompt = """
                Here are some hashtag suggestions for the image:
            """

            response = get_gemini_response(input_prompt, image_data, caption_prompt, hashtag_prompt)
            st.subheader("GenAI Response:")
            st.write(response)



#=====================================================================================================================
# Page: Meal Detail
def meal_detail_page():

    model3=genai.GenerativeModel('gemini-1.5-flash')

   #image means the image of the invoice  #user_prompt means the question asked by the user
    def get_gemini_response(input,image,user_prompt):  
        response=model3.generate_content([input,image[0],user_prompt])
        return response.text



    #conversion of image data into bytes
    def input_image_details(uploaded_file):
        if uploaded_file is not None:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()

            image_parts = [
                {
                    "mime_type": uploaded_file.type,  # get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")
        
    st.header("Meal Details 🍝")
    st.write("Welcome to the Meal Details.")
    st.write("You can ask any questions about the food and I will try to answer it.")
    
    input=st.text_input("Enter the query... ",key="input")
    uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image=Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit=st.button("Tell me...")

    input_prompt="""
    You are an expert in understanding invoices. We will upload a a image as various food items, cuisines, dishes
    and you will have to answer any questions based on the uploaded food image. User may ask what is 
    the colorie, fat etc you need to answer it in tabular format. Atleast you have to detect the food items
    and give a rough idea... please do this
    """

    ## if submit button is clicked

    if submit:
        if uploaded_file:
            image_data=input_image_details(uploaded_file)
            response=get_gemini_response(input_prompt,image_data,input)
            st.subheader("The Rresponse is")
            st.write(response)
        else:
            st.error("Please upload the meal image")

#=====================================================================================================================
## outfit maker

import streamlit as st
from PIL import Image
import google.generativeai as genai

def outfit_maker_page():

    def get_gemini_response(input, image, prompt):
        model10 = genai.GenerativeModel('gemini-1.5-flash')  # Update model name
        response = model10.generate_content([input, image[0], prompt])
        return response.text

    def input_image_setup(uploaded_file):
        if uploaded_file is not None:
            try:
                bytes_data = uploaded_file.getvalue()
                image_parts = [
                    {
                        "mime_type": uploaded_file.type,
                        "data": bytes_data
                    }
                ]
                return image_parts
            except Exception as e:
                st.error(f"Error processing image: {e}")
                return None  # Indicate error
        else:
            raise FileNotFoundError("No file uploaded")

    st.header("Outfit Maker 👕")
    input = st.radio("Choose the input type", ["Male", "Female", "Kid"])
    input = st.text_input("Enter the outfit related query.... ", key="input")
    uploaded_file = st.file_uploader("Choose an image that constains you outfit (like top + bottom + footwear + other accessories. )...", type=["jpg", "jpeg", "png"])
    image = ""

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about it....")

    input_prompt = """

    You are an expert in fashion industry and you are a great fashion infuence where you need to see the outfit from the image and recommend the best suited color of pants with different shirts or foowears other other dress of men and womer in the image.
    You also have to provide the details of every outfit items with the color and brand of the outfit.
    Also you give the score to the outfit based on the color combination and the brand of the outfit out of 10.
    Use may enter the input section and may ask some questions related to outfit then you have to answer all of them..
    Also you have to recommend the improvement for the outfit.
    Also you have to response to the user query in the form of the outfit details.
    you have to generate all the responses in the form of
    if you found top then you have to provide the details of the top with color, brand, score and recommended for improvement.
    1. Item 1 - color - brand - score - recommended for improvement
    if you found bottom then you have to provide the details of the top with color, brand, score and recommended for improvement.
    2. Item 2 - color - brand - score - recommended for improvement
    if you found footwear then you have to provide the details of the top with color, brand, score and recommended for improvement.
    3. Item 3 - color - brand - score - recommended for improvement
    if you found other accessories like watches jewellery etc then you have to provide the details of the top with color, brand, score and recommended for improvement.
    4. Item 4 - color - brand - score - recommended for improvement
    ----
    ----
    And at last you have to give the overall score of the outfit based on the color combination and the brand of the outfit out of 10.
    And the best place suited for the clothing eg., wedding party, office, casual etc.

    """

    if submit:
        if uploaded_file:
            image_data = input_image_setup(uploaded_file)
            try:
                response = get_gemini_response(input_prompt, image_data, input)
                st.subheader("The Response is")
                st.write(response)
            except Exception as e:
                st.error(f"Error generating response: {e}")
        else:
            st.write("Please upload the image to get the response, as the image is not uploaded.")
#=====================================================================================================================
## aesthetic rating

def aesthetic_rating_page():
    def get_gemini_repsonse(input,image,prompt):
        model11=genai.GenerativeModel('gemini-1.5-flash')
        response=model11.generate_content([input,image[0],prompt])
        return response.text
    

    #conversion of image data to bytes
    def input_image_setup(uploaded_file):
        # Check if a file has been uploaded
        if uploaded_file is not None:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()  # Read the file into bytes

            image_parts = [
                {
                    "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")

    st.header("Aesthetic Rating 🦸‍♀️")
    input=st.radio("Choose the input type",["Male", "Female", "Kid"])
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)


    submit=st.button("Tell me about it....")

    input_prompt="""

    You are an expert in fashion industry and you are a great fashion infuence, instagram fashion influence and a great model where you need to see the outfit, model pose, background, aestheticeness from the image and recommend the best pose with different outfits and other environments and backgrounds other dress of men or womer in the image.
    You also have to give the different pose for the model.
    You also have to give the different background for the model image.
    You also have to give the different image filters for the model image.
    You also have to give the different camera angles for the model image.
    You also have to give the different dress for the model image.
    Also you have to response to the user query in the form of the aesthiticness.
    you have to generate all the responses in the form of 
    
    pose - backgrounf of the image - filter - environment- outfit- style - aestheticness score on the scale of 1 to 10 - is this photo good to upload on instagram or any other social media platform Yes/No (percentage).
    
    ----
    ----        
    At last of you have to tell how can model his her photoshoot image and aesthetic image eg., wedding party, office, casual etc.
    please give rating in tabular format    
    """

    ## If submit button is clicked

    if submit:
        if uploaded_file:
            image_data=input_image_setup(uploaded_file)
            response=get_gemini_repsonse(input_prompt,image_data,input)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the image to get the response, as the image is not uploaded.")
#=====================================================================================================================


#=====================================================================================================================  
# Page: ATS Score Check
def ats_score_check_page():
    def get_gemini_response(input):
        model5 = genai.GenerativeModel('gemini-pro')
        response = model5.generate_content(input)
        response_dict = json.loads(response.text)
    
        # Extract JD Match percentage
        jd_match = response_dict.get("JD Match", "N/A")
        
        # Extract Missing Keywords list
        missing_keywords = response_dict.get("MissingKeywords", [])
        
        # Extract Profile Summary
        profile_summary = response_dict.get("Profile Summary", "N/A")
        
        # Create a formatted response string
        formatted_response = f"JD Match: {jd_match}\nMissing Keywords: {missing_keywords}\nProfile Summary: {profile_summary}"
        
        return formatted_response

    def input_pdf_text(uploaded_file):
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            text += str(page.extract_text())
        return text

    # Prompt Template
    input_prompt = """
        Hey Act Like a skilled or very experienced ATS (Application Tracking System)
        with a deep understanding of the tech field, software engineering, data science, data analysis,
        and big data engineering. Your task is to evaluate the resume based on the given job description.
        You must consider the job market is very competitive and you should provide the
        best assistance for improving the resumes. Assign the percentage Matching based 
        on JD and
        the missing keywords with high accuracy.
        resume:{text}
        description:{jd}

        I want the response in one single string having the structure
        {{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
        """    

        ## streamlit app
    st.title("Gen ATS")
    st.text("Improve Your Resume ATS score")
    jd = st.text_area("Paste the Job Description....")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

    submit = st.button("Submit")    

    if submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            input_str = input_prompt.format(text=text, jd=jd)
            response = get_gemini_response(input_str)
            st.subheader(response)
                
        

#==================================================================================================================
# Page: YouTube se Padhai
def youtube_study_page():
    
    prompt="""You are Yotube video summarizer. You are provoded with various languages like english
    hindi, tamil, bangali etc..You will be taking the transcript text
    and summarizing the entire video and providing the important summary in points
    within 250 words. Please provide the summary of the text given here:... You need to provide summary either
      in english or hindi language..  """


    ## getting the transcript data from yt videos
    def extract_transcript_details(youtube_video_url):
        try:
            video_id=youtube_video_url.split("=")[1]
            
            transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

            transcript = ""
            for i in transcript_text:
                transcript += " " + i["text"]

            return transcript

        except Exception as e:
            raise e
        
    ## getting the summary based on Prompt from Google Gemini Pro
    def generate_gemini_content(transcript_text,prompt):

        model=genai.GenerativeModel("gemini-pro")
        response=model.generate_content(prompt+transcript_text)
        return response.text

    st.title("YouTube Transcript to Detailed Notes Converter")
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if youtube_link:
        video_id = youtube_link.split("=")[1]
        print(video_id)
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Get Detailed Notes"):
        transcript_text=extract_transcript_details(youtube_link)

        if transcript_text:
            summary=generate_gemini_content(transcript_text,prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)


#-----------------------------------------------------------------------------------------------------------

def about_the_author():
    author_name = "Rishi Ranjan"
    author_description = textwrap.dedent(
        """
        Date-->  19/04/2024
        🌟 **About Me:**
        https://www.linkedin.com/in/rishi-rih/

🚀 Hey there! I'm Rishi, a 2nd year passionate Computer Science & Engineering Undergraduate with a keen interest in the vast world of technology. Currently specializing in AI and Machine Learning, I'm on a perpetual quest for knowledge and thrive on learning new skills.

💻 My journey in the tech realm revolves around programming, problem-solving, and staying on the cutting edge of emerging technologies. With a strong foundation in Computer Science, I'm driven by the exciting intersection of innovation and research.

🔍 Amidst the digital landscape, I find myself delving into the realms of Blockchain, crafting Android Applications, and ML projects.
 JAVA and Python . 
My GitHub profile (https://github.com/RiH-137) showcases my ongoing commitment to refining my craft and contributing to the tech community.

🏎️ Outside the digital realm, I'm a fervent Formula 1 enthusiast, experiencing the thrill of high-speed pursuits. When I'm not immersed in code or cheering for my favorite F1 team, you might find me strategizing moves on the chessboard.

📧 Feel free to reach out if you're as passionate about technology as I am. You can connect with me at 101rishidsr@gmail.com.

Let's build, innovate, and explore the limitless possibilities of technology together! 🌐✨
        """
    )

    #caling the func that display name and description
    st.write(f"**Author:** {author_name}")
    st.write(author_description)
    
#==================================================================================================
import streamlit as st
from PIL import Image
import google.generativeai as genai

def image_to_code_page():
    # Function to generate code based on an image and selected code type
    def get_code_from_image(image, code_type):
        # Update the model to a version like "gemini-1.5-flash" or another generative AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Customize the prompt based on the selected code type
        if code_type == "HTML/CSS/JavaScript/React":
            prompt = "Generate a responsive webpage code (HTML, CSS, JavaScript, React) based on the contents of this image."
        elif code_type == "Python/Tinkercad":
            prompt = "Generate Python code or Tinkercad circuit design code based on the contents of this image."
        elif code_type == "Kotlin":
            prompt = "Generate a Kotlin application based on the contents of this image."
        
        # Generate the response
        response = model.generate_content([prompt, image])
        return response.text
    
    st.header("Image-to-Code Generator 🖼️➡️💻")
    st.text("Upload an image and receive code in your chosen language or framework.")

    # File uploader for the image
    uploaded_file = st.file_uploader("Upload an image (jpg, png, etc.)", type=["jpg", "jpeg", "png"])

    # Selectbox for code type selection
    code_type = st.selectbox(
        "Select the type of code to generate:",
        ("HTML/CSS/JavaScript/React", "Kotlin")
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Generate button to trigger code generation
        generate_code = st.button("Generate Code")

        if generate_code:
            # Get the code from the image based on the selected code type
            code_response = get_code_from_image(image, code_type)
            st.subheader(f"Generated {code_type} Code")
            
            # Use st.code() for code block output, with language based on the selected type
            if code_type == "HTML/CSS/JavaScript/React":
                st.code(code_response, language="html")
            
            elif code_type == "Kotlin":
                st.code(code_response, language="kotlin")
    else:
        st.write("Please upload an image to generate code.")


#------------------------------------------------------------------------------------------------------------------








# Sidebar navigation
pages = {
    "Chintu GPT": chintu_gpt_page,
    "Chintu GPT V2": chintu_gpt_v2_page,
    # "PDF se Padhai": input_pdf_text,
    "Image to Text": img_to_text,
    "Invoice Extractor": invoice_extractor_page,
    "Meal Detail": meal_detail_page,
    "ATS Score Check": ats_score_check_page,
    "Debug Code": debugger_page,
    "Image to Code": image_to_code_page,
    "YouTube se Padhai": youtube_study_page,
    "Outfit Maker": outfit_maker_page,
    "Aesthetic Rating": aesthetic_rating_page,
    "Pic Comparision": pic_comparison,
    # "Image Generation": image_generation_page,
    "About the Author": about_the_author,
    "Debug Code": debugger_page,
    
}

st.set_page_config(page_title="Student Vikaash",page_icon="1.png",layout="wide")
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select a Page", tuple(pages.keys()))

# Display the selected page
pages[selected_page]()



