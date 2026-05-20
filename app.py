import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Internship Resume Matcher")

st.title("AI Internship Resume Matcher for Data Science & Generative AI Roles")

st.write("Paste your resume and internship job description below.")

resume = st.text_area("Paste Resume Here", height=250)

job_description = st.text_area("Paste Job Description Here", height=250)

system_prompt = """
You are an AI career assistant specialized in Data Science, Machine Learning, and Generative AI internships.

Your job is to:
- compare resumes with internship descriptions
- identify missing technical skills
- recommend improvements
- suggest interview preparation tips

Rules:
- be honest and specific
- never invent experience
- focus on internships for students and early-career candidates
"""

required_skills = """
Important Data Science and AI internship skills:
Python
SQL
Machine Learning
Data Analysis
Statistics
Excel
Power BI
Tableau
Pandas
Scikit-learn
TensorFlow
GitHub
Streamlit
Generative AI
Communication
Problem Solving
"""

if st.button("Analyze"):

    if not resume or not job_description:
        st.warning("Please fill both fields.")

    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        prompt = f"""
{system_prompt}

Required Internship Skills:
{required_skills}

Resume:
{resume}

Job Description:
{job_description}

Return output in this format:

1. Match Score: X/100

2. Matching Skills:
- skill 1
- skill 2

3. Missing Skills:
- skill 1
- skill 2

4. Resume Improvements:
- suggestion 1
- suggestion 2

5. Interview Questions:
- question 1
- question 2
"""

        response = model.generate_content(prompt)

        st.subheader("Analysis")

        st.write(response.text)
