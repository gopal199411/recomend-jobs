# accounts/views.py

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .models import OTP, OTPPurpose

from .serializers import (
    SignupOTPSerializer,
    CreateUserSerializer,
    VerifyOTPSerializer,
    LoginSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    UserSerializer,
)

from .services import OTPService


User = get_user_model()



# ==================================
# SEND SIGNUP OTP
# ==================================

class SendSignupOTPAPIView(APIView):

    permission_classes = [
        AllowAny
    ]


    def post(self, request):

        serializer = SignupOTPSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )


        email = serializer.validated_data["email"]


        # Store temporary signup data in session for the verify step
        request.session["signup_data"] = {
            "username": serializer.validated_data["username"],
            "email": email,
            "phone_number": serializer.validated_data.get(
                "phone_number",
                ""
            ),
            "password": serializer.validated_data["password"],
        }


        otp = OTPService.create_otp(
            email,
            OTPPurpose.SIGNUP
        )


        OTPService.send_otp_email(
            email,
            otp.otp
        )


        return Response(
            {
                "message":
                "Signup OTP sent successfully"
            },
            status=status.HTTP_200_OK
        )



# ==================================
# VERIFY SIGNUP OTP AND CREATE USER
# ==================================

class VerifySignupOTPAPIView(APIView):

    permission_classes = [
        AllowAny
    ]


    def post(self, request):

        serializer = VerifyOTPSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )


        email = serializer.validated_data["email"]

        otp = serializer.validated_data["otp"]



        otp_obj = OTP.objects.filter(

            email=email,

            otp=otp,

            purpose=OTPPurpose.SIGNUP,

            is_verified=False

        ).first()



        if not otp_obj:

            return Response(
                {
                    "message":
                    "Invalid OTP"
                },
                status=status.HTTP_400_BAD_REQUEST
            )



        if not otp_obj.is_valid():

            return Response(
                {
                    "message":
                    "OTP expired"
                },
                status=status.HTTP_400_BAD_REQUEST
            )



        otp_obj.is_verified = True

        otp_obj.save()



        # Get temporary signup data
        signup_data = request.session.get(
            "signup_data"
        )


        if not signup_data:

            return Response(
                {
                    "message":
                    "Signup data expired. Register again."
                },
                status=status.HTTP_400_BAD_REQUEST
            )



        create_serializer = CreateUserSerializer(
            data=signup_data
        )


        create_serializer.is_valid(
            raise_exception=True
        )


        user = create_serializer.save()



        request.session.pop(
            "signup_data"
        )



        return Response(
            {
                "message":
                "Registration successful",

                "user":
                UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )



# ==================================
# LOGIN
# ==================================

class LoginAPIView(APIView):

    permission_classes = [
        AllowAny
    ]


    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        user = serializer.validated_data["user"]


        refresh = RefreshToken.for_user(
            user
        )


        return Response(
            {
                "refresh":
                str(refresh),

                "access":
                str(refresh.access_token),

                "user":
                UserSerializer(user).data
            },
            status=status.HTTP_200_OK
        )



# ==================================
# FORGOT PASSWORD SEND OTP
# ==================================

class ForgotPasswordAPIView(APIView):

    permission_classes = [
        AllowAny
    ]


    def post(self, request):

        serializer = ForgotPasswordSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        email = serializer.validated_data["email"]


        otp = OTPService.create_otp(
            email,
            OTPPurpose.FORGOT_PASSWORD
        )


        OTPService.send_otp_email(
            email,
            otp.otp
        )


        return Response(
            {
                "message":
                "Password reset OTP sent"
            },
            status=status.HTTP_200_OK
        )



# ==================================
# VERIFY FORGOT PASSWORD OTP
# ==================================

class VerifyForgotPasswordOTPAPIView(APIView):

    permission_classes = [
        AllowAny
    ]


    def post(self, request):

        serializer = VerifyOTPSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        email = serializer.validated_data["email"]

        otp = serializer.validated_data["otp"]



        success = OTPService.verify_otp(
            email,
            otp,
            OTPPurpose.FORGOT_PASSWORD
        )



        if not success:

            return Response(
                {
                    "message":
                    "Invalid OTP"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


        return Response(
            {
                "message":
                "OTP verified"
            },
            status=status.HTTP_200_OK
        )



# ==================================
# RESET PASSWORD
# ==================================

class ResetPasswordAPIView(APIView):

    permission_classes = [
        AllowAny
    ]


    def post(self, request):

        serializer = ResetPasswordSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        email = serializer.validated_data["email"]

        password = serializer.validated_data["new_password"]



        try:

            user = User.objects.get(
                email=email
            )


        except User.DoesNotExist:

            return Response(
                {
                    "message":
                    "User not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )



        user.set_password(
            password
        )

        user.save()



        return Response(
            {
                "message":
                "Password reset successful"
            },
            status=status.HTTP_200_OK
        )



# ==================================
# PROFILE
# ==================================

class ProfileAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        serializer = UserSerializer(
            request.user
        )

        return Response(
            {
                "user":
                serializer.data
            }
        )