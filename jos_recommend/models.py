from django.db import models


class JobRecommendation(models.Model):
    """
    Stores recommended jobs for candidates.
    """

    STATUS_CHOICES = [
        ("Recommended", "Recommended"),
        ("Applied", "Applied"),
        ("Rejected", "Rejected"),
        ("Expired", "Expired"),
    ]

    candidate = models.ForeignKey(
        "candidate.Candidate",
        on_delete=models.CASCADE,
        related_name="job_recommendations",
    )

    resume = models.ForeignKey(
        "resume.Resume",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="job_recommendations",
    )

    job = models.ForeignKey(
        "job_description.JobDescription",
        on_delete=models.CASCADE,
        related_name="job_recommendations",
    )

    match_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
    )

    skill_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
    )

    experience_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
    )

    education_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
    )

    location_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
    )

    matched_skills = models.JSONField(
        default=list,
        blank=True,
    )

    missing_skills = models.JSONField(
        default=list,
        blank=True,
    )

    recommendation_reason = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Recommended",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "job_recommendations"
        ordering = ["-match_score", "-created_at"]
        verbose_name = "Job Recommendation"
        verbose_name_plural = "Job Recommendations"
        constraints = [
            models.UniqueConstraint(
                fields=["candidate", "job"],
                name="unique_candidate_job"
            )
        ]

    def __str__(self):
        return f"{self.candidate} -> {self.job} ({self.match_score}%)"