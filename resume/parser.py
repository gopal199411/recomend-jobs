import re
import pdfplumber
from docx import Document


# =====================================================
# PDF Reader
# =====================================================

def extract_text_from_pdf(file_path):

    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print(f"PDF Parsing Error: {e}")

    return text


# =====================================================
# DOCX Reader
# =====================================================

def extract_text_from_docx(file_path):

    text = ""

    try:
        document = Document(file_path)

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

    except Exception as e:
        print(f"DOCX Parsing Error: {e}")

    return text


# =====================================================
# Resume Reader
# =====================================================

def parse_resume(file_path):

    extension = file_path.split(".")[-1].lower()

    if extension == "pdf":
        return extract_text_from_pdf(file_path)

    elif extension in ["doc", "docx"]:
        return extract_text_from_docx(file_path)

    return ""


# =====================================================
# Skill Extraction
# =====================================================

def extract_skills(text):

    skill_database = [
        "python",
        "django",
        "django rest framework",
        "drf",
        "rest api",
        "html",
        "css",
        "bootstrap",
        "javascript",
        "react",
        "angular",
        "java",
        "spring boot",
        "mysql",
        "postgresql",
        "sqlite",
        "git",
        "github",
        "docker",
        "aws",
        "linux",
        "machine learning",
        "tensorflow",
        "pytorch",
    ]

    text = text.lower()

    skills = []

    for skill in skill_database:
        if skill.lower() in text:
            skills.append(skill)

    return list(set(skills))


# =====================================================
# Email
# =====================================================

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    emails = re.findall(pattern, text)

    return emails[0] if emails else ""


# =====================================================
# Phone
# =====================================================

def extract_phone(text):

    pattern = r"(?:\+91[- ]?)?[6-9]\d{9}"

    phones = re.findall(pattern, text)

    return phones[0] if phones else ""


# =====================================================
# Summary
# =====================================================

def extract_summary(text):

    lines = text.split("\n")

    return " ".join(lines[:5])


# =====================================================
# Education
# =====================================================

def extract_education(text):

    keywords = [
        "b.e",
        "b.tech",
        "m.e",
        "m.tech",
        "b.sc",
        "m.sc",
        "mba",
        "bca",
        "mca",
    ]

    result = []

    for line in text.split("\n"):
        for keyword in keywords:
            if keyword.lower() in line.lower():
                result.append(line.strip())

    return result


# =====================================================
# Experience
# =====================================================

def extract_experience(text):

    result = []

    for line in text.split("\n"):
        if "experience" in line.lower():
            result.append(line.strip())

    return result


# =====================================================
# Languages
# =====================================================

def extract_languages(text):

    languages = [
        "Tamil",
        "English",
        "Hindi",
        "Telugu",
        "Malayalam",
        "Kannada",
    ]

    result = []

    for language in languages:
        if language.lower() in text.lower():
            result.append(language)

    return result


# =====================================================
# Projects
# =====================================================

def extract_projects(text):
    return []


# =====================================================
# Certifications
# =====================================================

def extract_certifications(text):
    return []


# =====================================================
# Main Parser
# =====================================================

def parse_resume_data(file_path):

    text = parse_resume(file_path)

    return {

        "extracted_text": text,

        "summary": extract_summary(text),

        "skills": extract_skills(text),

        "education": extract_education(text),

        "experience": extract_experience(text),

        "projects": extract_projects(text),

        "certifications": extract_certifications(text),

        "languages": extract_languages(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

    }