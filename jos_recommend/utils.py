import re


# ==========================================
# Normalize Text
# ==========================================

def normalize_text(text):
    """
    Convert text into clean lowercase format
    """

    if not text:
        return ""

    return str(text).lower().strip()



# ==========================================
# Clean Skills
# ==========================================

def clean_skills(skills):
    """
    Remove unwanted spaces
    Convert skills to lowercase
    """

    if not skills:
        return []


    cleaned = []

    for skill in skills:

        skill = normalize_text(skill)

        if skill:
            cleaned.append(skill)


    return cleaned



# ==========================================
# Extract Keywords From Job Description
# ==========================================

def extract_keywords(text):

    """
    Extract important words from text
    """

    text = normalize_text(text)


    words = re.findall(
        r"[a-zA-Z0-9+#.]+",
        text
    )


    stop_words = {

        "and",
        "or",
        "the",
        "with",
        "for",
        "to",
        "a",
        "an",
        "of",
        "in",
        "on",
        "is",
        "are",
        "required"

    }


    keywords = [

        word

        for word in words

        if word not in stop_words

    ]


    return list(set(keywords))



# ==========================================
# Skill Match Percentage
# ==========================================

def calculate_match_percentage(
        candidate_skills,
        required_skills
):

    """
    Calculate percentage of skill match
    """


    candidate_skills = set(
        clean_skills(candidate_skills)
    )


    required_skills = set(
        clean_skills(required_skills)
    )


    if not required_skills:

        return 0



    matched_skills = (
        candidate_skills
        &
        required_skills
    )


    score = int(

        (
            len(matched_skills)
            /
            len(required_skills)

        )
        * 100

    )


    return score



# ==========================================
# Get Matched Skills
# ==========================================

def get_matched_skills(
        candidate_skills,
        job_skills
):

    candidate_skills = set(
        clean_skills(candidate_skills)
    )


    job_skills = set(
        clean_skills(job_skills)
    )


    return list(
        candidate_skills
        &
        job_skills
    )



# ==========================================
# Get Missing Skills
# ==========================================

def get_missing_skills(
        candidate_skills,
        job_skills
):

    candidate_skills = set(
        clean_skills(candidate_skills)
    )


    job_skills = set(
        clean_skills(job_skills)
    )


    return list(
        job_skills
        -
        candidate_skills
    )