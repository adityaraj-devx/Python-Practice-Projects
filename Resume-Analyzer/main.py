import io
import os 
import PyPDF2
from groq import Groq
import streamlit as stm
from dotenv import load_dotenv

load_dotenv()

stm.set_page_config(page_title="Resume Analyzer", page_icon="🗒️", layout="centered")

stm.title("Resume-Analyzer")
stm.markdown("Upload to get an AI-powered analysis of the resume.")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

uploaded_file = stm.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = stm.text_input("Enter the job role yor're targetting (optional)")

analyze = stm.button("Start Analysis")

def extract_text_from_pdf(pdf):
    pdf_reader = PyPDF2.PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        if not file_content.strip():
            stm.error("File does not have any contect")
            stm.stop()

        prompt = f"""
        You are an experienced ATS recruiter.

        Analyze this resume as if it were being screened by an Applicant Tracking System.

        Evaluate:

        1. ATS Compatibility Score (0-100)
        2. Keyword optimization
        3. Missing keywords for {job_role if job_role else "software engineering roles"}
        4. Resume formatting issues
        5. Section ordering
        6. Readability
        7. Action verbs used
        8. Quantifiable achievements
        9. Technical skills relevance
        10. Final ATS pass probability

        Resume:

        {file_content}

        Respond with clear headings and bullet points.
        """

        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[
                {"role": "system", "content": "You are an experienced ATS recruiter"},
                {"role": "user", "content": prompt}
            ],
        temperature=0
        )

        stm.markdown("-----------Analysis Result-----------")
        stm.markdown(response.choices[0].message.content)

    except Exception as e:
        stm.error(f"An error occured: {str(e)}")