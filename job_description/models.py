from django.db import models



# =====================================================
# Job Description Model
# =====================================================

class JobDescription(models.Model):
    """
    Stores company job descriptions / vacancies
    """


    STATUS_CHOICES = (

        ("OPEN", "Open"),

        ("CLOSED", "Closed"),

        ("EXPIRED", "Expired"),

    )


    JOB_TYPE_CHOICES = (

        ("FULL_TIME", "Full Time"),

        ("PART_TIME", "Part Time"),

        ("CONTRACT", "Contract"),

        ("INTERNSHIP", "Internship"),

        ("FREELANCE", "Freelance"),

    )


    # -----------------------------
    # Basic Job Information
    # -----------------------------

    title = models.CharField(

        max_length=255

    )


    company_name = models.CharField(

        max_length=255

    )


    location = models.CharField(

        max_length=255,

        blank=True

    )


    salary = models.CharField(

        max_length=100,

        blank=True

    )


    job_type = models.CharField(

        max_length=50,

        choices=JOB_TYPE_CHOICES,

        default="FULL_TIME"

    )


    status = models.CharField(

        max_length=50,

        choices=STATUS_CHOICES,

        default="OPEN"

    )


    # -----------------------------
    # Experience Requirement
    # -----------------------------

    minimum_experience = models.IntegerField(

        default=0

    )


    maximum_experience = models.IntegerField(

        null=True,

        blank=True

    )


    # -----------------------------
    # Education Requirement
    # -----------------------------

    education = models.CharField(

        max_length=255,

        blank=True

    )


    # -----------------------------
    # Job Description Content
    # -----------------------------

    description = models.TextField(

        blank=True

    )


    # Uploaded JD file

    jd_file = models.FileField(

        upload_to="job_descriptions/",

        null=True,

        blank=True

    )


    # Extracted text from JD parser

    extracted_text = models.TextField(

        blank=True,

        null=True

    )


    # -----------------------------
    # Skills
    # -----------------------------

    required_skills = models.JSONField(

        default=list,

        blank=True

    )


    preferred_skills = models.JSONField(

        default=list,

        blank=True

    )


    # -----------------------------
    # AI / Matching Fields
    # -----------------------------

    experience_keywords = models.JSONField(

        default=list,

        blank=True

    )


    responsibilities = models.JSONField(

        default=list,

        blank=True

    )


    qualifications = models.JSONField(

        default=list,

        blank=True

    )


    # -----------------------------
    # Timestamps
    # -----------------------------

    created_at = models.DateTimeField(

        auto_now_add=True

    )


    updated_at = models.DateTimeField(

        auto_now=True

    )



    class Meta:

        db_table = "job_descriptions"


        ordering = [

            "-created_at"

        ]


        verbose_name = "Job Description"


        verbose_name_plural = "Job Descriptions"



    def __str__(self):

        return f"{self.title} - {self.company_name}"