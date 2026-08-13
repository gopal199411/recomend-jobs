import uuid
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone


# ==========================================================
# OTP PURPOSE
# ==========================================================

class OTPPurpose(models.TextChoices):
    PRE_SIGNUP = "PRE_SIGNUP", "Pre-signup Email Verification"
    SIGNUP = "SIGNUP", "Signup"
    FORGOT_PASSWORD = "FORGOT_PASSWORD", "Forgot Password"


# ==========================================================
# OTP MODEL
# ==========================================================

class OTP(models.Model):
    email = models.EmailField()

    otp = models.CharField(
        max_length=6,
    )

    purpose = models.CharField(
        max_length=30,
        choices=OTPPurpose.choices,
    )

    expires_at = models.DateTimeField()

    is_verified = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "recruiter_otps"

        ordering = ["-created_at"]

        indexes = [
            models.Index(
                fields=["email", "purpose"],
                name="otp_email_purpose_idx",
            ),
            models.Index(
                fields=["email", "is_verified"],
                name="otp_email_verify_idx",
            ),
        ]

    def is_valid(self):
        return (
            not self.is_verified
            and self.expires_at > timezone.now()
        )

    def __str__(self):
        return f"{self.email} - {self.purpose}"


# ==========================================================
# RECRUITER PROFILE
# ==========================================================

class RecruiterProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recruiter_profile",
    )

    # ------------------------------------------------------
    # Recruiter Information
    # ------------------------------------------------------

    full_name = models.CharField(
        max_length=150,
    )

    recruiter_name = models.CharField(
        max_length=150,
    )

    designation = models.CharField(
        max_length=150,
        blank=True,
    )

    # ------------------------------------------------------
    # Company Information
    # ------------------------------------------------------

    company_name = models.CharField(
        max_length=200,
    )

    industry_type = models.CharField(
        max_length=100,
        blank=True,
    )

    company_website = models.URLField(
        blank=True,
    )

    # ------------------------------------------------------
    # Contact Information
    # ------------------------------------------------------

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )

    # ------------------------------------------------------
    # Location
    # ------------------------------------------------------

    company_location = models.CharField(
        max_length=200,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

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

    # ------------------------------------------------------
    # Profile Information
    # ------------------------------------------------------

    bio = models.TextField(
        blank=True,
    )

    # ------------------------------------------------------
    # Online Status
    # ------------------------------------------------------

    is_online = models.BooleanField(
        default=False,
    )

    last_seen = models.DateTimeField(
        default=timezone.now,
    )

    # ------------------------------------------------------
    # Timestamps
    # ------------------------------------------------------

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "recruiter_profiles"

        ordering = ["-created_at"]

        indexes = [
            models.Index(
                fields=["email"],
                name="recruiter_email_idx",
            ),
            models.Index(
                fields=["company_name"],
                name="recruiter_company_idx",
            ),
            models.Index(
                fields=["is_online"],
                name="recruiter_online_idx",
            ),
        ]

    def __str__(self):
        return self.recruiter_name or self.full_name


# ==========================================================
# RECRUITER HEADER PROFILE
# ==========================================================

class RecruiterHeaderProfile(models.Model):

    recruiter_profile = models.OneToOneField(
        RecruiterProfile,
        on_delete=models.CASCADE,
        related_name="header",
    )

    # ------------------------------------------------------
    # Images
    # ------------------------------------------------------

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

    # ------------------------------------------------------
    # Header Information
    # ------------------------------------------------------

    website = models.URLField(
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

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

    bio = models.TextField(
        blank=True,
    )

    # ------------------------------------------------------
    # Online Status
    # ------------------------------------------------------

    is_online = models.BooleanField(
        default=False,
    )

    last_seen = models.DateTimeField(
        default=timezone.now,
    )

    # ------------------------------------------------------
    # Timestamps
    # ------------------------------------------------------

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "recruiter_header_profiles"

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.recruiter_profile.full_name} Header"


# ==========================================================
# PASSWORD RESET TOKEN
# ==========================================================

class PasswordResetToken(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recruiter_password_reset_tokens",
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_used = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "recruiter_password_reset_tokens"

        ordering = ["-created_at"]

        indexes = [
            models.Index(
                fields=["user", "is_used"],
                name="reset_user_used_idx",
            ),
        ]

    def save(self, *args, **kwargs):
        if self.expires_at is None:
            self.expires_at = (
                timezone.now() + timedelta(minutes=15)
            )

        super().save(*args, **kwargs)

    def is_valid(self):
        return (
            not self.is_used
            and self.expires_at is not None
            and self.expires_at > timezone.now()
        )

    def __str__(self):
        return f"Password reset - {self.user}"