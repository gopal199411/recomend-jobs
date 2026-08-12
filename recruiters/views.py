<<<<<<< HEAD
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .models import RecruiterProfile
from .permissions import IsRecruiter
from .serializers import (
    RecruiterLoginSerializer,
    RecruiterProfileSerializer,
    RecruiterRegisterSerializer,
)


class RecruiterRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RecruiterRegisterSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        profile = serializer.save()
=======
import secrets
from datetime import timedelta

from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    OTP,
    OTPPurpose,
    PasswordResetToken,
    RecruiterHeaderProfile,
)
from .permissions import HasRecruiterProfile, IsRecruiter
from .serializers import (
    ForgotPasswordOTPVerifySerializer,
    ForgotPasswordSerializer,
    RecruiterHeaderProfileSerializer,
    RecruiterLoginSerializer,
    RecruiterProfileSerializer,
    RecruiterSignupSerializer,
    ResetPasswordSerializer,
    SignupOTPVerifySerializer,
)

User = get_user_model()


def generate_otp():
    return str(secrets.randbelow(900000) + 100000)


def send_otp_email(email, otp, purpose):
    send_mail(
        subject=f"Recruiter {purpose} OTP",
        message=f"Your OTP is {otp}. It expires in 10 minutes.",
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
    )


class RecruiterSignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RecruiterSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        otp = generate_otp()

        OTP.objects.filter(
            email=user.email,
            purpose=OTPPurpose.SIGNUP,
        ).delete()

        OTP.objects.create(
            email=user.email,
            otp=otp,
            purpose=OTPPurpose.SIGNUP,
            expires_at=timezone.now() + timedelta(minutes=10),
        )

        send_otp_email(user.email, otp, "Signup")
>>>>>>> e2ad693 (commit msg)

        return Response(
            {
                "success": True,
<<<<<<< HEAD
                "message": "Recruiter registration successful",
                "profile": serializer.data,
=======
                "message": "Signup successful. OTP sent to your email.",
>>>>>>> e2ad693 (commit msg)
            },
            status=status.HTTP_201_CREATED,
        )


<<<<<<< HEAD
=======
class RecruiterSignupOTPVerifyAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupOTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        otp_value = serializer.validated_data["otp"]

        otp = OTP.objects.filter(
            email=email,
            otp=otp_value,
            purpose=OTPPurpose.SIGNUP,
            is_verified=False,
            expires_at__gt=timezone.now(),
        ).first()

        if not otp:
            return Response(
                {"detail": "Invalid or expired OTP."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(
            email=email,
            role="RECRUITER",
        ).first()

        if not user:
            return Response(
                {"detail": "Recruiter account not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        otp.is_verified = True
        otp.save(update_fields=["is_verified"])

        user.is_active = True
        user.save(update_fields=["is_active"])

        return Response(
            {
                "success": True,
                "message": "Email verified successfully. You can now login.",
            },
            status=status.HTTP_200_OK,
        )


>>>>>>> e2ad693 (commit msg)
class RecruiterLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RecruiterLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

<<<<<<< HEAD
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(
            request=request,
            username=username,
            password=password,
        )

        if user is None:
            return Response(
                {
                    "success": False,
                    "detail": "Invalid username or password.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user.role != "EMPLOYER":
            return Response(
                {
                    "success": False,
                    "detail": "This account is not a recruiter account.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        try:
            profile = user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "detail": "Recruiter profile not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

=======
        user = authenticate(
            request=request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response(
                {"detail": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user.role != "RECRUITER":
            return Response(
                {"detail": "This is not a recruiter account."},
                status=status.HTTP_403_FORBIDDEN,
            )

        if not user.is_active:
            return Response(
                {"detail": "Please verify your email before login."},
                status=status.HTTP_403_FORBIDDEN,
            )

        header = user.recruiter_profile.header
        header.is_online = True
        header.last_seen = timezone.now()
        header.save(update_fields=["is_online", "last_seen"])
>>>>>>> e2ad693 (commit msg)
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "success": True,
<<<<<<< HEAD
                "message": "Recruiter login successful.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "recruiter": {
                    "full_name": profile.full_name,
                    "email": profile.email,
                    "role": "Recruiter",
                },
=======
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_200_OK,
        )


class RecruiterLogoutAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsRecruiter,
        HasRecruiterProfile,
    ]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            RefreshToken(refresh_token).blacklist()
        except TokenError:
            return Response(
                {"detail": "Invalid or expired refresh token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        header = request.user.recruiter_profile.header
        header.is_online = True
        header.last_seen = timezone.now()
        header.save(update_fields=["is_online", "last_seen"])

        return Response(
            {
                "success": True,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_200_OK,
        )

class RecruiterForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        user = User.objects.filter(
            email=email,
            role="RECRUITER",
        ).first()

        if not user:
            return Response(
                {"detail": "Recruiter account not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        otp_value = generate_otp()

        OTP.objects.filter(
            email=email,
            purpose=OTPPurpose.FORGOT_PASSWORD,
        ).delete()

        OTP.objects.create(
            email=email,
            otp=otp_value,
            purpose=OTPPurpose.FORGOT_PASSWORD,
            expires_at=timezone.now() + timedelta(minutes=10),
        )

        send_otp_email(email, otp_value, "Forgot Password")

        return Response(
            {
                "success": True,
                "message": "Password-reset OTP sent to your email.",
            },
            status=status.HTTP_200_OK,
        )


class RecruiterForgotPasswordOTPVerifyAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordOTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        otp_value = serializer.validated_data["otp"]

        otp = OTP.objects.filter(
            email=email,
            otp=otp_value,
            purpose=OTPPurpose.FORGOT_PASSWORD,
            is_verified=False,
            expires_at__gt=timezone.now(),
        ).first()

        if not otp:
            return Response(
                {"detail": "Invalid or expired OTP."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(
            email=email,
            role="RECRUITER",
        ).first()

        otp.is_verified = True
        otp.save(update_fields=["is_verified"])

        reset_token = PasswordResetToken.objects.create(user=user)

        return Response(
            {
                "success": True,
                "message": "OTP verified successfully.",
                "reset_token": str(reset_token.token),
            },
            status=status.HTTP_200_OK,
        )


class RecruiterResetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reset_token = PasswordResetToken.objects.filter(
            token=serializer.validated_data["reset_token"],
            is_used=False,
            expires_at__gt=timezone.now(),
        ).first()

        if not reset_token:
            return Response(
                {"detail": "Invalid or expired reset token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = reset_token.user
        user.set_password(serializer.validated_data["password"])
        user.save()

        reset_token.is_used = True
        reset_token.save(update_fields=["is_used"])

        return Response(
            {
                "success": True,
                "message": "Password reset successful.",
>>>>>>> e2ad693 (commit msg)
            },
            status=status.HTTP_200_OK,
        )


class RecruiterProfileAPIView(APIView):
<<<<<<< HEAD
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request):
        try:
            profile = request.user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {"detail": "Recruiter profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = RecruiterProfileSerializer(
            profile,
            context={"request": request},
        )

        return Response(
            {
                "success": True,
                "data": serializer.data,
            },
=======
    permission_classes = [
        IsAuthenticated,
        IsRecruiter,
        HasRecruiterProfile,
    ]

    def get(self, request):
        serializer = RecruiterProfileSerializer(
            request.user.recruiter_profile,
        )

        return Response(
            {"success": True, "data": serializer.data},
>>>>>>> e2ad693 (commit msg)
            status=status.HTTP_200_OK,
        )

    def patch(self, request):
<<<<<<< HEAD
        try:
            profile = request.user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {"detail": "Recruiter profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = RecruiterProfileSerializer(
            profile,
            data=request.data,
            partial=True,
            context={"request": request},
        )

=======
        serializer = RecruiterProfileSerializer(
            request.user.recruiter_profile,
            data=request.data,
            partial=True,
        )
>>>>>>> e2ad693 (commit msg)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "success": True,
<<<<<<< HEAD
                "message": "Recruiter profile updated successfully.",
=======
                "message": "Profile updated successfully.",
>>>>>>> e2ad693 (commit msg)
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


<<<<<<< HEAD
class RecruiterHeaderAPIView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request):
        try:
            profile = request.user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "detail": "Recruiter profile not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        profile_image = None

        if profile.profile_image:
            profile_image = request.build_absolute_uri(
                profile.profile_image.url
=======
class RecruiterHeaderProfileAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsRecruiter,
        HasRecruiterProfile,
    ]

    def get(self, request):
        header = request.user.recruiter_profile.header

        profile_image = None
        if header.profile_image:
            profile_image = request.build_absolute_uri(
                header.profile_image.url
>>>>>>> e2ad693 (commit msg)
            )

        return Response(
            {
                "success": True,
<<<<<<< HEAD
                "full_name": profile.full_name,
                "role": "Recruiter",
                "profile_image": profile_image,
            },
            status=status.HTTP_200_OK,
        )
=======
                "full_name": request.user.recruiter_profile.full_name,
                "role": "Recruiter",
                "profile_image": profile_image,
                "is_online": header.is_online,
                "status": "online" if header.is_online else "offline",
            },
            status=status.HTTP_200_OK,
        )

    def patch(self, request):
        serializer = RecruiterHeaderProfileSerializer(
            request.user.recruiter_profile.header,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Header profile updated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
>>>>>>> e2ad693 (commit msg)
