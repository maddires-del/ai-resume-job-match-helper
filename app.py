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
prompt = f"""
Required Internship Skills:
{required_skills}

Resume:
{resume}

Job Description:
{job_description}
"""

response = model.generate_content(prompt)
