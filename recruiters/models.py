<<<<<<< HEAD
=======
import uuid
from datetime import timedelta

>>>>>>> e2ad693 (commit msg)
from django.conf import settings
from django.db import models
from django.utils import timezone
``

<<<<<<< HEAD
=======
class OTPPurpose(models.TextChoices):
    SIGNUP = "SIGNUP", "Signup"
    FORGOT_PASSWORD = "FORGOT_PASSWORD", "Forgot Password"


class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    purpose = models.CharField(
        max_length=30,
        choices=OTPPurpose.choices,
    )
    expires_at = models.DateTimeField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "recruiter_otps"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["email", "purpose"]),
        ]

    def is_valid(self):
        return not self.is_verified and self.expires_at > timezone.now()

    def __str__(self):
        return f"{self.email} - {self.purpose}"


>>>>>>> e2ad693 (commit msg)
class RecruiterProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recruiter_profile",
    )

    full_name = models.CharField(max_length=150)
<<<<<<< HEAD
    company_name = models.CharField(max_length=200)

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15,
        blank=True,
=======
    recruiter_name = models.CharField(max_length=150, blank=True)
    designation = models.CharField(max_length=150, blank=True)

    company_name = models.CharField(max_length=200)
    company_website = models.URLField(blank=True)
    company_location = models.CharField(max_length=200, blank=True)
    industry_type = models.CharField(max_length=100, blank=True)

    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "recruiter_profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return self.recruiter_name or self.full_name


class RecruiterHeaderProfile(models.Model):
    recruiter_profile = models.OneToOneField(
        RecruiterProfile,
        on_delete=models.CASCADE,
        related_name="header",
>>>>>>> e2ad693 (commit msg)
    )

    profile_image = models.ImageField(
        upload_to="recruiters/profile_images/",
        blank=True,
        null=True,
    )
<<<<<<< HEAD

=======
>>>>>>> e2ad693 (commit msg)
    company_logo = models.ImageField(
        upload_to="recruiters/company_logos/",
        blank=True,
        null=True,
    )

<<<<<<< HEAD
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
    
    
=======
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "recruiter_header_profiles"

    def __str__(self):
        return f"{self.recruiter_profile.full_name} Header"


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
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "recruiter_password_reset_tokens"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=15)
        super().save(*args, **kwargs)

    def is_valid(self):
        return not self.is_used and self.expires_at > timezone.now()
>>>>>>> e2ad693 (commit msg)
