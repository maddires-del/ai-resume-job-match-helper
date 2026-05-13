import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Resume + Job Match Helper")

st.title("AI Resume + Job Match Helper")

st.write("Paste your resume and job description below.")

resume = st.text_area("Paste Resume Here", height=250)

job_description = st.text_area("Paste Job Description Here", height=250)

if st.button("Analyze"):

    if not resume or not job_description:
        st.warning("Please fill both fields.")

    else:

        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        system_prompt = """
        You are an AI career assistant.
        Compare resumes with job descriptions.
        Be honest and simple.
        Do not invent experience.
        """

        user_prompt = f"""
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

        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=system_prompt,
            input=user_prompt
        )

        st.subheader("Analysis")

        st.write(response.output_text)
