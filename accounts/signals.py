from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Candidate

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    """Automatically create the relevant profile when a new user is created."""
    if not created:
        return

    role = getattr(instance, "role", None)

    if role == "CANDIDATE":
        Candidate.objects.get_or_create(
            user=instance,
        )
    elif role == "EMPLOYER":
        # Lazy import to avoid circular imports at module load time.
        from recruiters.models import RecruiterProfile

        RecruiterProfile.objects.get_or_create(
            user=instance,
            defaults={
                "full_name": instance.get_full_name() or instance.username,
                "email": instance.email,
                "phone_number": instance.phone_number or "",
                "designation": "",
                "company_name": "",
            },
        )
