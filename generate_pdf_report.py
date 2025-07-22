from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

# Your data (can also import from main.py if modular)
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

# Create PDF
pdf_path = "skill_gap_report.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

# Header
c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, "🎯 Resume Skill Match Report")

c.setFont("Helvetica", 12)
c.drawString(50, height - 80, f"Name: {resume_name}")
c.drawString(50, height - 100, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Section titles
c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 140, f"📌 Extracted Skills ({len(extracted_skills)}):")
c.setFont("Helvetica", 12)
c.drawString(70, height - 160, ", ".join(extracted_skills))

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 200, f"✅ Matched Skills ({len(matched_skills)}):")
c.setFont("Helvetica", 12)
c.drawString(70, height - 220, ", ".join(matched_skills))

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 260, f"❌ Missing Skills ({len(missing_skills)}):")
c.setFont("Helvetica", 12)
c.drawString(70, height - 280, ", ".join(missing_skills))

# Recommendation
c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 320, "📢 Recommendation:")
c.setFont("Helvetica", 12)
c.drawString(70, height - 340, "Learn missing skills to match top company hiring needs.")

# Save PDF
c.save()
print(f"✅ PDF report generated and saved as '{pdf_path}'")
