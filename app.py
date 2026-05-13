import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Resume + Job Match Helper")

st.title("AI Resume + Job Match Helper")

st.write("Paste your resume and job description below.")

resume = st.text_area("Paste Resume Here", height=250)

job_description = st.text_area("Paste Job Description Here", height=250)

if st.button("Analyze"):

    if not resume or not job_description:
        st.warning("Please fill both fields.")

    else:

        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

        model = genai.GenerativeModel("gemini-2.0-flash")

        prompt = f"""
        You are an AI career assistant.

        Compare this resume with the job description.

        Be honest and simple.
        Do not invent experience.

        Resume:
        {resume}

        Job Description:
        {job_description}

        Give:
        1. Match score
        2. Matching skills
        3. Missing skills
        4. Resume improvements
        5. Interview questions
        """

        response = model.generate_content(prompt)

        st.subheader("Analysis")

        st.write(response.text)
