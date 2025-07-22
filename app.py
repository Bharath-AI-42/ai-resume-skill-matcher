import streamlit as st
import PyPDF2
import re
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64

# -------------------------------
# Page Config and CSS Styling
# -------------------------------
st.set_page_config(page_title="AI Resume Skill Matcher", layout="wide")

# Background & layout styling
st.markdown("""
    <style>
        body {
            background-color: white;
        }
        .main {
            background-image: url("https://wallpapercave.com/wp/wp3497433.jpg");
            background-size: cover;
            background-position: top;
            padding: 2rem;
        }
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
        }
        .left-align {
            text-align: left;
            padding-left: 30px;
        }
        .highlight {
            font-weight: bold;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Logo and Title (Landing)
# -------------------------------
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("logo.png", width=120)
st.title("AI Resume Skill Matcher")
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# Resume Upload Section
# -------------------------------
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    # -------------------------------
    # Step 1: Skill Extraction
    # -------------------------------
    skill_keywords = [
        "python", "java", "c", "c++", "html", "css", "javascript", "node.js",
        "typescript", "angular", "django", "sql", "aws", "windows", "linux",
        "git", "github", "docker", "machine learning", "deep learning", "opencv"
    ]
    required_skills = ["python", "java", "c", "html", "css", "javascript", "django", "sql", "aws", "git", "github", "docker"]

    cleaned_resume = re.sub(r'[^a-zA-Z0-9\s\.\-]', '', resume_text.lower())
    found_skills = [skill for skill in skill_keywords if skill in cleaned_resume]
    matched_skills = [s for s in found_skills if s in required_skills]
    missing_skills = [s for s in required_skills if s not in found_skills]

    # -------------------------------
    # Resume Summary Display
    # -------------------------------
    st.markdown('<div class="left-align">', unsafe_allow_html=True)
    st.subheader("✅ Extracted Skills")
    st.markdown(f"<p class='highlight'>{', '.join(found_skills) if found_skills else 'None detected'}</p>", unsafe_allow_html=True)

    st.subheader("❌ Missing Important Skills")
    st.markdown(f"<p class='highlight'>{', '.join(missing_skills) if missing_skills else 'None!'}</p>", unsafe_allow_html=True)

    # -------------------------------
    # Step 2: Job Domain Suggestion
    # -------------------------------
    job_domains = {
        "Web Development": ["html", "css", "javascript", "django", "node.js", "typescript", "angular"],
        "Machine Learning Engineer": ["python", "machine learning", "deep learning", "opencv"],
        "DevOps Engineer": ["git", "github", "docker", "aws", "linux"],
        "Data Analyst": ["python", "sql"],
        "Backend Developer": ["java", "node.js", "sql", "docker"],
        "Cybersecurity": ["linux", "aws", "python"]
    }

    st.subheader("💼 Suggested Job Domains")
    suggested_domains = []
    for domain, skills in job_domains.items():
        if any(skill in found_skills for skill in skills):
            suggested_domains.append(domain)

    if suggested_domains:
        for domain in suggested_domains:
            st.markdown(f"✅ <b>{domain}</b>", unsafe_allow_html=True)
    else:
        st.markdown("⚠️ No strong domain suggestions based on current skills.")

    # -------------------------------
    # Step 3: Learning + Job Links
    # -------------------------------
    st.subheader("📚 Learn Missing Skills")
    learn_links = {
        "git": "https://www.codecademy.com/learn/learn-git",
        "github": "https://lab.github.com/",
        "docker": "https://docker-curriculum.com/",
        "sql": "https://www.w3schools.com/sql/",
        "aws": "https://www.aws.training/"
    }

    for skill in missing_skills:
        if skill in learn_links:
            st.markdown(f"🔗 <b>{skill.upper()}</b>: [Learn here]({learn_links[skill]})", unsafe_allow_html=True)

    st.subheader("🌐 Apply for Jobs")
    st.markdown("🔗 [Internshala](https://internshala.com/jobs)")
    st.markdown("🔗 [LinkedIn Jobs](https://www.linkedin.com/jobs)")
    st.markdown("🔗 [Indeed](https://www.indeed.com)")
    st.markdown("🔗 [Naukri](https://www.naukri.com)")

    # -------------------------------
    # Step 4: PDF Report Download
    # -------------------------------
    if st.button("⬇️ Download Skill Report as PDF"):
        pdf_file = "skill_gap_report.pdf"
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.drawString(100, 750, f"AI Resume Skill Match Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        c.drawString(100, 720, f"Extracted Skills: {', '.join(found_skills)}")
        c.drawString(100, 700, f"Missing Skills: {', '.join(missing_skills)}")
        c.drawString(100, 680, f"Suggested Domains: {', '.join(suggested_domains)}")
        c.save()

        with open(pdf_file, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="skill_gap_report.pdf">📥 Click here to download PDF</a>'
            st.markdown(href, unsafe_allow_html=True)

    # -------------------------------
    # Step 5: Rating (Star-Based)
    # -------------------------------
    st.subheader("⭐ Rate This App")
    rating = st.radio("Please rate from 1 to 5 stars", [1, 2, 3, 4, 5], horizontal=True)
    st.write(f"You rated this app: {rating} ⭐")

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("👆 Upload your resume PDF to get started.")