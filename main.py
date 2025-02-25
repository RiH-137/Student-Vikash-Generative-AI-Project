# import sys
# from pathlib import Path
# import streamlit as st

# # Add the project root directory to sys.path
# project_root = Path(__file__).parent
# sys.path.append(str(project_root))

# # Import page functions
# from pages.chintu_gpt import chintu_gpt_page
# from pages.chintu_gpt_v2 import chintu_gpt_v2_page
# from pages.debugger import debugger_page
# from pages.ats_score import ats_score_check_page
# from pages.invoice_extractor import invoice_extractor_page
# from pages.img_to_text import img_to_text
# from pages.pic_comparison import pic_comparison
# from pages.meal_detail import meal_detail_page
# from pages.outfit_maker import outfit_maker_page
# from pages.aesthetic_rating import aesthetic_rating_page
# from pages.youtube_study import youtube_study_page
# from pages.image_to_code import image_to_code_page
# from pages.about_author import about_the_author

# # Page configuration
# st.set_page_config(page_title="Student Vikaash", page_icon="1.png", layout="wide")

# # Dictionary of pages
# pages = {
#     "Chintu GPT": chintu_gpt_page,
#     "Chintu GPT V2": chintu_gpt_v2_page,
#     "Debug Code": debugger_page,
#     "ATS Score Check": ats_score_check_page,
#     "Invoice Extractor": invoice_extractor_page,
#     "Image to Text": img_to_text,
#     "Pic Comparision": pic_comparison,
#     "Meal Detail": meal_detail_page,
#     "Outfit Maker": outfit_maker_page,
#     "Aesthetic Rating": aesthetic_rating_page,
#     "YouTube se Padhai": youtube_study_page,
#     "Image to Code": image_to_code_page,
#     "About the Author": about_the_author,
# }

# # Sidebar navigation
# st.sidebar.title("Navigation")
# selected_page = st.sidebar.radio("Select a Page", tuple(pages.keys()))

# # Run the selected page
# pages[selected_page]()