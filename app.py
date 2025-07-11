import streamlit as st
import PyPDF2
import re

# -------------------------------
# Page Title
# -------------------------------
st.set_page_config(page_title="AI Resume Skill Matcher", layout="centered")
st.title("📄 AI Resume Skill Matcher")
st.write("Upload your resume (PDF) and find out what skills are detected!")

# -------------------------------
# Skill Keywords
# -------------------------------
skill_keywords = [
    "python", "java", "c", "c++", "html", "css", "javascript", "node.js",
    "typescript", "angular", "django", "sql", "aws", "windows", "linux",
    "git", "github", "machine learning", "deep learning", "opencv"
]

# -------------------------------
# PDF Upload Section
# -------------------------------
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")

if uploaded_file:
    # Read PDF content
    reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()

    st.subheader("📜 Resume Content")
    st.text_area("Extracted Text:", resume_text, height=250)

    # Clean and process text
    resume_text_lower = re.sub(r'[^a-zA-Z0-9\s\.\-]', '', resume_text.lower())

    # Extract matching skills
    found_skills = []
    for skill in skill_keywords:
        if skill in resume_text_lower:
            found_skills.append(skill)

    st.subheader("✅ Extracted Skills")
    if found_skills:
        st.success(", ".join(found_skills))
    else:
        st.warning("No matching skills found.")
