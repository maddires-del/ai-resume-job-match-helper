if st.button("Run Agent"):

    if not resume or not job_description:
        st.warning("Please fill both fields.")

    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        routing_prompt = f"""
You are an AI agent.

Choose ONE tool from:
1. Analyze Job Fit
2. Improve Resume Bullets
3. Write Recruiter Message

Return ONLY the tool name.

User Goal: analyze and help with internship application

Resume:
{resume}

Job Description:
{job_description}
"""

        route = model.generate_content(routing_prompt).text.strip()

        st.subheader("Selected Tool")
        st.write(route)
        if "Analyze Job Fit" in route:

            prompt = f"""
{system_prompt}

Task: Analyze Job Fit

Resume:
{resume}

Job Description:
{job_description}

Return:
Match score, matching skills, missing skills, recommendations.
"""

        elif "Improve Resume" in route:

            prompt = f"""
{system_prompt}

Task: Improve Resume Bullets

Resume:
{resume}

Job Description:
{job_description}

Rewrite bullets without inventing experience.
"""

        elif "Recruiter Message" in route:

            prompt = f"""
{system_prompt}

Task: Write Recruiter Message

Resume:
{resume}

Job Description:
{job_description}

Write a short professional outreach message.
"""

        response = model.generate_content(prompt)

        st.subheader("Agent Output")
        st.write(response.text)

## Agent Design

This system uses a 2-step agent pipeline:

1. Routing Step:
   The model selects the most appropriate tool:
   - Analyze Job Fit
   - Improve Resume Bullets
   - Write Recruiter Message

2. Execution Step:
   The selected tool is executed using a structured prompt.

This design improves flexibility and simulates real-world AI agent behavior.
