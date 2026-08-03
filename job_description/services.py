from .models import JobDescription

from .utils import (
    clean_text,
    extract_skills,
    extract_experience,
    extract_keywords,
)



# =====================================================
# Parse Job Description
# =====================================================

def parse_job_description(job):

    """
    Extract information from Job Description
    """


    text = ""


    if job.description:

        text = job.description


    elif job.extracted_text:

        text = job.extracted_text



    cleaned_text = clean_text(text)



    skills = extract_skills(
        cleaned_text
    )


    experience = extract_experience(
        cleaned_text
    )


    keywords = extract_keywords(
        cleaned_text
    )



    return {

        "extracted_text": cleaned_text,

        "required_skills": skills,

        "minimum_experience": experience,

        "experience_keywords": keywords,

    }





# =====================================================
# Update Parsed JD Data
# =====================================================

def update_job_description_data(job_id):

    """
    Parse and save extracted JD information
    """


    try:

        job = JobDescription.objects.get(
            id=job_id
        )


    except JobDescription.DoesNotExist:

        return None



    parsed_data = parse_job_description(
        job
    )



    job.extracted_text = (
        parsed_data[
            "extracted_text"
        ]
    )


    job.required_skills = (
        parsed_data[
            "required_skills"
        ]
    )


    job.minimum_experience = (
        parsed_data[
            "minimum_experience"
        ]
    )


    job.experience_keywords = (
        parsed_data[
            "experience_keywords"
        ]
    )


    job.save()



    return job





# =====================================================
# Create Job Description
# =====================================================

def create_job_description(data):

    """
    Create new job and auto parse skills
    """


    job = JobDescription.objects.create(

        title=data.get(
            "title"
        ),

        company_name=data.get(
            "company_name"
        ),

        location=data.get(
            "location",
            ""
        ),

        salary=data.get(
            "salary",
            ""
        ),

        job_type=data.get(
            "job_type",
            "FULL_TIME"
        ),

        description=data.get(
            "description",
            ""
        ),

        required_skills=data.get(
            "required_skills",
            []
        ),

        preferred_skills=data.get(
            "preferred_skills",
            []

        )

    )


    # Auto parse JD

    update_job_description_data(
        job.id
    )


    return job





# =====================================================
# Job Skill Matching
# =====================================================

def match_candidate_with_job(
        candidate_skills,
        job
):

    """
    Compare candidate skills
    with job required skills
    """


    candidate_skills = [

        skill.lower()

        for skill in candidate_skills

    ]


    required_skills = [

        skill.lower()

        for skill in job.required_skills

    ]



    matched_skills = list(

        set(candidate_skills)

        &

        set(required_skills)

    )



    missing_skills = list(

        set(required_skills)

        -

        set(candidate_skills)

    )



    if required_skills:

        score = (

            len(matched_skills)

            /

            len(required_skills)

        ) * 100


    else:

        score = 0



    return {

        "match_score": round(
            score,
            2
        ),

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

    }





# =====================================================
# Recommend Jobs
# =====================================================

def recommend_jobs(candidate):

    """
    Generate job recommendations
    """


    jobs = JobDescription.objects.filter(
        status="OPEN"
    )


    results = []



    for job in jobs:


        result = match_candidate_with_job(

            candidate.skills,

            job

        )


        if result["match_score"] >= 30:


            results.append({

                "job": job,

                "match_score":
                result["match_score"],

                "matched_skills":
                result["matched_skills"],

                "missing_skills":
                result["missing_skills"],

            })



    return results