from django.urls import path

from .views import (
    SendSignupOTPAPIView,
    VerifySignupOTPAPIView,
    LoginAPIView,
    ForgotPasswordAPIView,
    VerifyForgotPasswordOTPAPIView,
    ResetPasswordAPIView,
    ProfileAPIView,
)


app_name = "accounts"


urlpatterns = [
    # Candidate signup - send OTP
    path(
        "send-signup-otp/",
        SendSignupOTPAPIView.as_view(),
        name="send-signup-otp",
    ),

    # Candidate signup - verify OTP and create user
    path(
        "verify-signup-otp/",
        VerifySignupOTPAPIView.as_view(),
        name="verify-signup-otp",
    ),

    # Login
    path(
        "login/",
        LoginAPIView.as_view(),
        name="login",
    ),

    # Forgot password - send OTP
    path(
        "forgot-password/",
        ForgotPasswordAPIView.as_view(),
        name="forgot-password",
    ),

    # Forgot password - verify OTP
    path(
        "verify-forgot-password-otp/",
        VerifyForgotPasswordOTPAPIView.as_view(),
        name="verify-forgot-password-otp",
    ),

    # Reset password
    path(
        "reset-password/",
        ResetPasswordAPIView.as_view(),
        name="reset-password",
    ),

    # Profile
    path(
        "profile/",
        ProfileAPIView.as_view(),
        name="profile",
    ),
]
