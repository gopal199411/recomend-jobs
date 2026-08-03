from django.db.models.signals import (
    post_save,
    pre_save
)

from django.dispatch import receiver

from job_description.models import JobDescription


# ==========================================
# Job Created Signal
# ==========================================

@receiver(
    post_save,
    sender=JobDescription
)
def job_created_signal(
        sender,
        instance,
        created,
        **kwargs
):

    """
    Runs after creating a new job
    """

    if created:

        print(
            f"New Job Created: {instance.title}"
        )



# ==========================================
# Job Status Change Signal
# ==========================================

@receiver(
    pre_save,
    sender=JobDescription
)
def job_status_change_signal(
        sender,
        instance,
        **kwargs
):

    """
    Track job status changes
    """

    if not instance.pk:
        return


    try:

        old_job = JobDescription.objects.get(
            pk=instance.pk
        )


        if old_job.status != instance.status:

            print(
                f"Job status changed: "
                f"{old_job.status} -> {instance.status}"
            )


    except JobDescription.DoesNotExist:

        pass

