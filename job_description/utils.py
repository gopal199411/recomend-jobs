import re



# =====================================================
# Clean Job Description Text
# =====================================================

def clean_text(text):
    """
    Remove unwanted characters
    and normalize JD text
    """

    if not text:
        return ""


    text = text.lower()


    text = re.sub(
        r"\s+",
        " ",
        text
    )


    text = re.sub(
        r"[^a-z0-9\s\+\#\.\-]",
        "",
        text
    )


    return text.strip()





# =====================================================
# Extract Skills From JD
# =====================================================

def extract_skills(text):

    """
    Extract technical skills from job description
    """

    skill_database = [

        "python",

        "django",

        "flask",

        "fastapi",

        "java",

        "javascript",

        "react",

        "angular",

        "node",

        "sql",

        "mysql",

        "postgresql",

        "mongodb",

        "rest api",

        "docker",

        "aws",

        "azure",

        "git",

        "github",

        "machine learning",

        "deep learning",

        "data science",

        "pandas",

        "numpy",

        "tensorflow",

        "pytorch",

    ]


    text = clean_text(text)


    found_skills = []


    for skill in skill_database:

        if skill in text:

            found_skills.append(skill)



    return found_skills





# =====================================================
# Extract Experience Requirement
# =====================================================

def extract_experience(text):

    """
    Extract years of experience
    Example:
    2 years experience
    """

    if not text:

        return 0


    pattern = r"(\d+)\+?\s*(?:years|year|yrs)"


    result = re.search(

        pattern,

        text.lower()

    )


    if result:

        return int(
            result.group(1)
        )


    return 0





# =====================================================
# Extract Job Title Keywords
# =====================================================

def extract_keywords(text):

    """
    Extract important words
    """

    text = clean_text(text)


    words = text.split()


    stop_words = [

        "the",

        "and",

        "with",

        "for",

        "required",

        "experience",

        "job",

        "role",

        "candidate",

    ]


    keywords = [

        word

        for word in words

        if word not in stop_words

    ]


    return list(
        set(keywords)
    )





# =====================================================
# Skill Match Percentage
# =====================================================

def calculate_skill_match(
        candidate_skills,
        job_skills
):

    """
    Calculate skill matching percentage
    """


    if not job_skills:

        return 0



    candidate_skills = [

        skill.lower()

        for skill in candidate_skills

    ]


    job_skills = [

        skill.lower()

        for skill in job_skills

    ]



    matched = set(
        candidate_skills
    ) & set(
        job_skills
    )



    score = (

        len(matched)

        /

        len(job_skills)

    ) * 100



    return round(
        score,
        2
    )





# =====================================================
# Missing Skills
# =====================================================

def find_missing_skills(
        candidate_skills,
        required_skills
):


    candidate_skills = [

        skill.lower()

        for skill in candidate_skills

    ]


    required_skills = [

        skill.lower()

        for skill in required_skills

    ]



    return list(

        set(required_skills)

        -

        set(candidate_skills)

    )