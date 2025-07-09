import PyPDF2
import re

# Step 1: Read the resume PDF
with open("Resume F.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()

# Step 2: Print resume text
print("------ RESUME CONTENT ------\n")
print(resume_text)

# Step 3: Define known skills
skill_keywords = [
    "python", "java", "c", "c++", "html", "css", "javascript", "nodejs", "node.js",
    "typescript", "angular", "django", "sql", "aws", "windows", "linux",
    "git", "github", "machine learning", "deep learning", "opencv", "docker"
]

# Step 4: Clean the resume text for matching
resume_cleaned = re.sub(r'[^a-zA-Z0-9\s]', ' ', resume_text.lower()).replace("node.js", "nodejs")

# Step 5: Match skills
found_skills = []
for skill in skill_keywords:
    normalized_skill = skill.replace(".", "")  # to match "node.js" and "nodejs"
    if normalized_skill in resume_cleaned.replace(".", ""):
        found_skills.append(skill)

# Step 6: Display extracted skills
print("\n------ EXTRACTED SKILLS FROM RESUME ------")
if found_skills:
    print(", ".join(sorted(set(found_skills))))
else:
    print("❌ No matching skills found.")
# -------------------------------
# Step 4: Compare with Job Description
# -------------------------------

# Load job description text
with open("job_description.txt", "r") as job_file:
    job_text = job_file.read().lower()

# Clean job text for matching
job_text_clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', job_text)

# Extract skills required in the job
required_skills = [skill for skill in skill_keywords if skill.replace('.', '') in job_text_clean.replace('.', '')]

# Compare with resume
matched_skills = [skill for skill in required_skills if skill in found_skills]
missing_skills = [skill for skill in required_skills if skill not in found_skills]

# Display report
print("\n------ SKILL MATCH REPORT ------")
print(f"✅ You already have ({len(matched_skills)}): {', '.join(matched_skills)}")
print(f"❌ You are missing ({len(missing_skills)}): {', '.join(missing_skills)}")
