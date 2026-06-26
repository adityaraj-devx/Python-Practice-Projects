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