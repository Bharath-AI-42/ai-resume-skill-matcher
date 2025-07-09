from datetime import datetime

# You can import from main.py instead in real projects
resume_name = "NAGARIKANTI VENKATA BHARATH"
extracted_skills = [
    "angular", "aws", "c", "css", "django", "html", "java",
    "javascript", "linux", "machine learning", "python", "sql",
    "typescript", "windows"
]
matched_skills = [
    "python", "java", "c", "html", "css", "javascript", "django", "sql", "aws"
]
missing_skills = ["git", "github", "docker"]

# Create report content
report = f"""
===============================
🎯 Resume Skill Match Report
===============================

Name: {resume_name}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📌 Skills Found in Resume ({len(extracted_skills)}):
{', '.join(extracted_skills)}

✅ Skills Matched with Job ({len(matched_skills)}):
{', '.join(matched_skills)}

❌ Skills Missing from Job Description ({len(missing_skills)}):
{', '.join(missing_skills)}

📢 Recommendation:
Focus on learning the missing skills (like Docker, Git/GitHub) to improve job match rate.

🔖 Built using: Python, PyPDF2, Regex
By: {resume_name}
"""

# Save to text file with UTF-8 encoding
with open("skill_gap_report.txt", "w", encoding="utf-8") as f:
    f.write(report.strip())

print("✅ Skill report saved as 'skill_gap_report.txt'")
