import os

from .models import Resume
from .parser import extract_skills



# =====================================================
# Resume Text Processing Service
# =====================================================

def process_resume_text(resume_id, extracted_text):
    """
    Process extracted resume text
    and update resume data
    """

    try:

        resume = Resume.objects.get(
            id=resume_id
        )

    except Resume.DoesNotExist:

        return None



    # Extract skills

    skills = extract_skills(
        extracted_text
    )



    resume.extracted_text = extracted_text

    resume.skills = skills

    resume.is_parsed = True


    resume.save()



    return resume





# =====================================================
# Skill Extraction Service
# =====================================================

def extract_resume_skills(text):
    """
    Extract skills from resume content
    """

    skills = extract_skills(
        text
    )


    return skills





# =====================================================
# Resume Data Update Service
# =====================================================

def update_resume_data(
        resume_id,
        data
):
    """
    Update parsed resume information
    """

    try:

        resume = Resume.objects.get(
            id=resume_id
        )

    except Resume.DoesNotExist:

        return None



    allowed_fields = [

        "summary",

        "skills",

        "education",

        "experience",

        "projects",

        "certifications",

        "languages",

        "ats_score",

    ]



    for field in allowed_fields:

        if field in data:

            setattr(
                resume,
                field,
                data[field]
            )



    resume.is_parsed = True


    resume.save()



    return resume





# =====================================================
# Resume Skill Matching Service
# =====================================================

def calculate_skill_match(
        resume_skills,
        job_skills
):
    """
    Compare resume skills
    with job required skills
    """


    resume_skills = [

        skill.lower()

        for skill in resume_skills

    ]


    job_skills = [

        skill.lower()

        for skill in job_skills

    ]



    matched = list(

        set(resume_skills)
        &
        set(job_skills)

    )


    missing = list(

        set(job_skills)
        -
        set(resume_skills)

    )



    if job_skills:

        score = (

            len(matched)

            /

            len(job_skills)

        ) * 100

    else:

        score = 0



    return {

        "match_score":
        round(score,2),

        "matched_skills":
        matched,

        "missing_skills":
        missing

    }





# =====================================================
# Resume File Validation Service
# =====================================================

def validate_resume_file(file):

    """
    Validate uploaded resume file
    """

    allowed_extensions = [

        "pdf",
        "doc",
        "docx"

    ]


    extension = (

        file.name
        .split(".")[-1]
        .lower()

    )


    if extension not in allowed_extensions:

        return False


    return True