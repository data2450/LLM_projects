import os
import random
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
# Set your Google API key directly (or load it from a .env file)
#GOOGLE_API_KEY = "AIzaSyAr8pmds414HHBFpUZXUvYq2SV5OmOCetU"  # Replace with your actual API key
#os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
# Initialize the Generative Model
genai.configure(api_key=GOOGLE_API_KEY)
flash = genai.GenerativeModel('gemini-2.0-flash')

# Function to generate unique cover letters
def generate_cover_letters(user_input):
    cover_letters = []
    
    for _ in range(5):
        # Add some randomness or variation in the prompt or parameters
        variation = random.choice([
            "Use a formal tone to describe the user's skills and experience.",
            "Use a creative and impactful approach to highlight the skills and experience.",
            "Write a brief and concise cover letter while emphasizing the user's skills.",
            "Adopt a professional tone while including achievements and past experiences.",
            "Focus on the key strengths that would be valuable for the job and company."
        ])
        
        prompt = f"Generate a professional cover letter based on the following details: {user_input}. {variation}"

        # Generate content based on the modified prompt
        response = flash.generate_content(prompt)
        
        # Append the generated cover letter to the list
        cover_letters.append(response.text)
    
    return cover_letters

# Function to rank cover letters
def rank_cover_letters(cover_letters):
    return sorted(cover_letters, key=len, reverse=True)  # Simple ranking by length

# Streamlit App
def main():
    st.title("Cover Letter Generator")
    
    # Input fields
    user_info = st.text_area("Enter your experience and skills:")
    company = st.text_input("Enter the company name:")
    job_description = st.text_area("Enter the job description:")
    
    if st.button("Generate Cover Letters"):
        user_input = f"User Information: {user_info}, Company: {company}, Job Description: {job_description}"
        
        cover_letters = generate_cover_letters(user_input)
        ranked_letters = rank_cover_letters(cover_letters)
        
        st.markdown("## **Generated Cover Letters (Ranked):**")
        for idx, letter in enumerate(ranked_letters, 1):
            st.write(f"\nCover Letter {idx}:\n{letter}\n")

if __name__ == "__main__":
    main()