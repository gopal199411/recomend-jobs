from django.core.exceptions import ValidationError



# =====================================================
# Validate Job Title
# =====================================================

def validate_job_title(value):

    if not value:

        raise ValidationError(
            "Job title is required."
        )


    if len(value.strip()) < 3:

        raise ValidationError(
            "Job title must contain at least 3 characters."
        )


    return value





# =====================================================
# Validate Company Name
# =====================================================

def validate_company_name(value):

    if not value:

        raise ValidationError(
            "Company name is required."
        )


    if len(value.strip()) < 2:

        raise ValidationError(
            "Company name is too short."
        )


    return value





# =====================================================
# Validate Job Description
# =====================================================

def validate_description(value):

    if not value:

        raise ValidationError(
            "Job description is required."
        )


    if len(value.strip()) < 20:

        raise ValidationError(
            "Job description must contain minimum 20 characters."
        )


    return value





# =====================================================
# Validate Skills
# =====================================================

def validate_skills(value):

    """
    Required skills should be a list
    Example:
    ["Python","Django","SQL"]
    """


    if not isinstance(value, list):

        raise ValidationError(
            "Skills must be provided as a list."
        )


    if len(value) == 0:

        raise ValidationError(
            "At least one skill is required."
        )


    for skill in value:

        if not isinstance(skill, str):

            raise ValidationError(
                "Each skill must be text."
            )


    return value





# =====================================================
# Validate Experience
# =====================================================

def validate_experience(
        minimum,
        maximum
):


    if minimum is not None:

        if minimum < 0:

            raise ValidationError(
                "Minimum experience cannot be negative."
            )



    if maximum is not None:

        if maximum < 0:

            raise ValidationError(
                "Maximum experience cannot be negative."
            )



    if (
        minimum is not None
        and maximum is not None
        and minimum > maximum
    ):

        raise ValidationError(
            "Minimum experience cannot be greater than maximum experience."
        )


    return True





# =====================================================
# Validate Salary
# =====================================================

def validate_salary(value):

    if not value:

        return value


    if len(value) > 100:

        raise ValidationError(
            "Salary information is too long."
        )


    return value





# =====================================================
# Validate Job File
# =====================================================

def validate_jd_file(file):

    """
    Allow PDF, DOC, DOCX JD files
    """


    allowed_extensions = [

        ".pdf",

        ".doc",

        ".docx",

    ]


    file_name = file.name.lower()



    if not any(
        file_name.endswith(ext)
        for ext in allowed_extensions
    ):

        raise ValidationError(
            "Only PDF, DOC, DOCX files are allowed."
        )


    return file