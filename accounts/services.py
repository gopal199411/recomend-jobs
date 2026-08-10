import random

from datetime import timedelta

from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from .models import OTP, OTPPurpose



class OTPService:


    # =========================
    # Generate 6 Digit OTP
    # =========================

    @staticmethod
    def generate_otp():

        return str(
            random.randint(
                100000,
                999999
            )
        )



    # =========================
    # Create OTP
    # =========================

    @staticmethod
    def create_otp(
        email,
        purpose
    ):

        otp = OTPService.generate_otp()


        # remove old OTP

        OTP.objects.filter(

            email=email,

            purpose=purpose,

            is_verified=False

        ).delete()



        otp_obj = OTP.objects.create(

            email=email,

            otp=otp,

            purpose=purpose,

            expires_at=

            timezone.now()
            +
            timedelta(minutes=5)

        )


        return otp_obj




    # =========================
    # Verify OTP
    # =========================

    @staticmethod
    def verify_otp(
        email,
        otp,
        purpose
    ):


        try:

            otp_obj = OTP.objects.get(

                email=email,

                otp=otp,

                purpose=purpose,

                is_verified=False

            )


        except OTP.DoesNotExist:

            return False



        if not otp_obj.is_valid():

            return False



        otp_obj.is_verified = True


        otp_obj.save(
            update_fields=[
                "is_verified"
            ]
        )


        return True





    # =========================
    # Send OTP Email
    # =========================

    @staticmethod
    def send_otp_email(
        email,
        otp
    ):


        subject = (
            "Password Reset OTP"
        )


        message = f"""

Hello,

Your OTP is : {otp}

OTP valid for 5 minutes.

Thank you.

"""


        send_mail(

            subject,

            message,

            settings.DEFAULT_FROM_EMAIL,

            [email],

            fail_silently=False

        )