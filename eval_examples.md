# Evaluation Examples

# What Good Looks Like

A good output should:
- Use the resume and job description correctly
- Not invent experience
- Identify matching and missing skills
- Give useful next steps
- Follow the selected agent action

---

## Test Case 1: Strong Data Science Internship Match

Selected Action:
Analyze Job Fit

Resume:
Master’s student in Data Science and Analytics with Python, SQL, Excel, Tableau, Machine Learning, GitHub, Streamlit, and Gemini API project experience.

Job Description:
Data Science Intern needed with Python, SQL, machine learning, data visualization, communication skills, and GitHub experience.

Expected:
High match score, strong technical alignment, and useful improvement suggestions.

Actual:
- The agent identified Python, SQL, Machine Learning, GitHub, and Streamlit as matching skills.
- The agent gave a strong match score.
- The agent suggested improving communication examples and adding more measurable project results.

Observation:
The agent worked well because it used both the resume, job description, and skill framework to produce a focused internship analysis.

---

## Test Case 2: Resume Bullet Improvement

Selected Action:
Improve Resume Bullets

Resume:
Built AI resume matcher using Streamlit and Gemini API. Used Python and GitHub.

Job Description:
AI Intern needed with Python, Generative AI, API integration, prompt engineering, and deployment experience.

Expected:
The agent should rewrite resume bullets using stronger action verbs without inventing experience.

Actual:
- The agent rewrote bullets to highlight Streamlit, Gemini API, prompt engineering, deployment, and GitHub.
- The agent kept the bullets realistic and did not invent fake company experience.

Observation:
This action worked well because it transformed basic resume points into stronger internship-ready bullet points.

---

## Test Case 3: Recruiter Message Generation

Selected Action:
Write Recruiter Message

Resume:
Data Science graduate student with Python, SQL, Machine Learning, Streamlit, and Gemini API project experience.

Job Description:
Hiring Data Science Interns with Python, SQL, machine learning, and communication skills.

Expected:
The agent should create a short and professional recruiter message.

Actual:
- The agent created a concise recruiter message.
- It mentioned the internship role and relevant skills.
- It kept the tone professional and simple.

Observation:
This action is useful because it supports a real application task, not just analysis.

---

## Test Case 4: Weak Resume for AI Role

Selected Action:
Analyze Job Fit

Resume:
Customer service experience, basic Excel, teamwork, scheduling.

Job Description:
Machine Learning Intern requiring Python, machine learning, Scikit-learn, TensorFlow, model evaluation, and GitHub.

Expected:
Low match score and clear missing technical skills.

Actual:
- The agent identified major missing skills such as Python, Machine Learning, Scikit-learn, TensorFlow, and GitHub.
- It recommended building beginner AI/ML projects before applying.
- It did not invent technical experience.

Observation:
The agent handled a weak match honestly and gave useful next steps.

---

## Test Case 5: Failure / Insufficient Information Case

Selected Action:
Analyze Job Fit

Resume:
Hardworking student looking for an internship.

Job Description:
We are hiring an intern.

Expected:
The agent should say there is not enough information instead of guessing.

Actual:
- The agent stated that the resume and job description were too vague.
- It asked for more details about skills, projects, tools, and role requirements.
- It avoided inventing experience or giving an unrealistic high score.

Observation:
This was a useful failure test because the agent showed uncertainty instead of making up details.
## Test Case 1: Internship Application Assistance

Resume:
Python, SQL, GitHub, Streamlit, Machine Learning

Job Description:
Data Science Internship

User Goal:
I want help applying for this internship.

Actual Output:
Selected Tool: Analyze Job Fit

Match Score:
Moderate

Correctly identified:
- Python
- SQL
- Machine Learning
- GitHub
- Streamlit

Missing Skills:
- Pandas
- NumPy
- Scikit-learn
- Statistics
- Data Visualization

Observation:
The agent selected the correct tool, explained its reasoning, identified missing skills, and provided actionable recommendations.

## Failure Case

Resume:
Hardworking student

Job Description:
AI Research Intern requiring TensorFlow and LLM fine-tuning

User Goal:
Help me apply for this internship

Actual Output:
The agent reported insufficient technical information and could not perform a meaningful evaluation.

Observation:
The system avoided inventing experience and correctly identified missing information.
