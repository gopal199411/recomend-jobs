from django.conf import settings
from django.db import models
from django.utils import timezone


class RecruiterProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recruiter_profile",
    )

    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=200)

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to="recruiters/profile_images/",
        blank=True,
        null=True,
    )

    company_logo = models.ImageField(
        upload_to="recruiters/company_logos/",
        blank=True,
        null=True,
    )

    website = models.URLField(blank=True)
    address = models.TextField(blank=True)

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    state = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    bio = models.TextField(blank=True)

    is_online = models.BooleanField(default=False)

    last_seen = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "recruiter_profiles"
        ordering = ["-created_at"]
        verbose_name = "Recruiter Profile"
        verbose_name_plural = "Recruiter Profiles"

    def __str__(self):
        return f"{self.full_name} ({self.company_name})"
    
    