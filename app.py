import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Internship Application Agent")

st.title("AI Internship Application Agent")
st.write("An agentic AI assistant for Data Science and Generative AI internship applications.")

resume = st.text_area("Paste your resume here", height=220)
job_description = st.text_area("Paste the job description here", height=220)

user_goal = st.text_input(
    "What do you need help with?",
    "I want help applying for this internship."
)

system_prompt = """
You are an AI Internship Application Agent.

You help users with:
- job fit analysis
- resume improvement
- recruiter messaging

Rules:
- Do not invent experience
- Be honest and specific
- Only use provided resume and job description
"""

# ---------------- MAIN BUTTON ---------------- #

if st.button("Run Agent"):

    if not resume or not job_description:
        st.warning("Please fill both resume and job description.")

    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        # =========================
        # STEP 1: ROUTING (AGENT DECISION)
        # =========================
        routing_prompt = f"""
You are an AI agent with 3 tools:

1. Analyze Job Fit → if user wants skill match analysis
2. Improve Resume Bullets → if user wants resume rewriting
3. Write Recruiter Message → if user wants outreach/email

IMPORTANT:
Pick ONLY ONE tool based on intent.
Return ONLY the tool name.

Resume:
{resume}

Job Description:
{job_description}
"""

        route = model.generate_content(routing_prompt).text.strip()

        st.subheader("Selected Tool")
        st.write(route)

        # =========================
        # STEP 2: TOOL EXECUTION
        # =========================

        if "Analyze Job Fit" in route:

            prompt = f"""
{system_prompt}

TASK: Analyze Job Fit

Resume:
{resume}

Job Description:
{job_description}

Return:
- Match Score
- Matching Skills
- Missing Skills
- Recommendations
"""

        elif "Improve Resume Bullets" in route:

            prompt = f"""
{system_prompt}

TASK: Improve Resume Bullets

Rewrite resume bullets to be stronger.
Do NOT invent experience.

Resume:
{resume}

Job Description:
{job_description}
"""

        elif "Write Recruiter Message" in route:

            prompt = f"""
{system_prompt}

TASK: Write Recruiter Message

Create a short professional message to recruiter.

Resume:
{resume}

Job Description:
{job_description}
"""

        else:
            prompt = f"""
{system_prompt}

TASK: Analyze Job Fit (fallback)

Resume:
{resume}

Job Description:
{job_description}
"""

        # =========================
        # STEP 3: FINAL OUTPUT
        # =========================

        response = model.generate_content(prompt)

        st.subheader("Agent Output")
        st.write(response.text)
