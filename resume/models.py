from django.db import models
from candidate.models import Candidate


# =====================================================
# Resume Model
# =====================================================

class Resume(models.Model):
    """
    Stores candidate uploaded resume
    """

    RESUME_TYPE_CHOICES = (
        ("PDF", "PDF"),
        ("DOC", "DOC"),
        ("DOCX", "DOCX"),
    )


    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="resumes"
    )


    resume_file = models.FileField(
        upload_to="resumes/"
    )


    resume_type = models.CharField(
        max_length=10,
        choices=RESUME_TYPE_CHOICES,
        blank=True
    )


    # Extracted resume content
    extracted_text = models.TextField(
        blank=True,
        null=True
    )


    # AI / Parser extracted data

    summary = models.TextField(
        blank=True,
        null=True
    )


    skills = models.JSONField(
        default=list,
        blank=True
    )


    education = models.JSONField(
        default=list,
        blank=True
    )


    experience = models.JSONField(
        default=list,
        blank=True
    )


    projects = models.JSONField(
        default=list,
        blank=True
    )


    certifications = models.JSONField(
        default=list,
        blank=True
    )


    languages = models.JSONField(
        default=list,
        blank=True
    )


    # ATS score

    ats_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )


    is_parsed = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        db_table = "resumes"

        ordering = [
            "-created_at"
        ]

        verbose_name = "Resume"

        verbose_name_plural = "Resumes"



    def __str__(self):

        return f"{self.candidate.full_name} Resume"