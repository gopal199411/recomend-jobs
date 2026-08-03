from django.db import models


# =====================================================
# Candidate Model
# =====================================================

class Candidate(models.Model):
    """
    Stores candidate profile information
    """

    ROLE_CHOICES = (

        ("CANDIDATE", "Candidate"),

        ("EMPLOYEE", "Employee"),

        ("STUDENT", "Student"),

    )


    full_name = models.CharField(
        max_length=255
    )


    email = models.EmailField(
        unique=True
    )


    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )


    skills = models.JSONField(
        default=list,
        blank=True
    )


    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default="CANDIDATE"
    )


    experience = models.IntegerField(
        default=0,
        help_text="Experience in years"
    )


    education = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


    preferred_job_type = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    preferred_location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


    resume_uploaded = models.BooleanField(
        default=False
    )


    is_active = models.BooleanField(
        default=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:

        db_table = "candidates"

        ordering = [
            "-created_at"
        ]

        verbose_name = "Candidate"

        verbose_name_plural = "Candidates"



    def __str__(self):

        return self.full_name