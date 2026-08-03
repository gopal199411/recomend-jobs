from datetime import date

from rest_framework.exceptions import ValidationError



# ==========================================
# Validate Experience Range
# ==========================================

def validate_experience(
        minimum_experience,
        maximum_experience
):
    """
    Check minimum and maximum experience
    """

    if minimum_experience < 0:
        raise ValidationError(
            "Minimum experience cannot be negative"
        )


    if maximum_experience < 0:
        raise ValidationError(
            "Maximum experience cannot be negative"
        )


    if (
        maximum_experience
        and
        minimum_experience > maximum_experience
    ):
        raise ValidationError(
            "Minimum experience cannot be greater than maximum experience"
        )



# ==========================================
# Validate Skills
# ==========================================

def validate_skills(skills):
    """
    Validate required/preferred skills
    """

    if skills is None:
        return


    if not isinstance(skills, list):
        raise ValidationError(
            "Skills must be a list"
        )


    if len(skills) == 0:
        raise ValidationError(
            "Skills list cannot be empty"
        )


    for skill in skills:

        if not isinstance(skill, str):

            raise ValidationError(
                "Each skill must be a string"
            )



# ==========================================
# Validate Job Title
# ==========================================

def validate_job_title(title):

    if not title:

        raise ValidationError(
            "Job title is required"
        )


    if len(title.strip()) < 3:

        raise ValidationError(
            "Job title must contain minimum 3 characters"
        )



# ==========================================
# Validate Application Deadline
# ==========================================

def validate_deadline(deadline):

    if deadline:

        if deadline < date.today():

            raise ValidationError(
                "Application deadline cannot be in the past"
            )



# ==========================================
# Validate Vacancies
# ==========================================

def validate_vacancies(vacancies):

    if vacancies <= 0:

        raise ValidationError(
            "Vacancies must be greater than zero"
        )



# ==========================================
# Validate Job Description
# ==========================================

def validate_description(description):

    if not description:

        raise ValidationError(
            "Job description is required"
        )


    if len(description.strip()) < 20:

        raise ValidationError(
            "Job description should contain minimum 20 characters"
        )