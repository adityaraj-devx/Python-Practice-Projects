# Resume Analyzer

Resume Analyzer is an AI-powered web application built using Python, Streamlit, and Groq. It allows users to upload their resumes in PDF or TXT format and receive a detailed ATS (Applicant Tracking System) analysis, helping them improve their resumes for job applications.

## Features

* Upload resumes in PDF or TXT format
* AI-powered resume analysis using Groq's Llama 3.3 70B model
* ATS Compatibility Score
* Keyword optimization analysis
* Job role-specific recommendations
* Resume formatting and readability review
* Technical skills evaluation
* ATS pass probability assessment
* Simple and intuitive Streamlit interface

## Requirements

* Python 3.12+
* Groq API Key

## Installation

### Clone the Repository

```bash
git clone https://github.com/adityaraj-devx/Python-Practice-Projects.git
cd Python-Practice-Projects
cd "Resume-Analyzer"
```

### Install Dependencies

```bash
uv sync
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the application:

```bash
 uv streamlit run main.py
```

The application will open in your default web browser.

### How to Use

1. Upload a resume in **PDF** or **TXT** format.
2. (Optional) Enter the job role you are targeting.
3. Click **Start Analysis**.
4. Review the AI-generated ATS analysis and recommendations.

## Analysis Includes

* ATS Compatibility Score
* Keyword Optimization
* Missing Keywords
* Resume Formatting Review
* Section Ordering
* Readability Analysis
* Action Verb Evaluation
* Technical Skills Assessment
* ATS Pass Probability

## Project Structure

```text
.
├── main.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
├── README.md
└── .venv/
```

## Technologies Used

* Python
* Streamlit
* Groq
* PyPDF2
* python-dotenv

## License

This project is licensed under the MIT License.
