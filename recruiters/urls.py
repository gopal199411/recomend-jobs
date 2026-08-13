from django.urls import path

from .views import (
    RecruiterSignupAPIView,
    RecruiterSignupOTPVerifyAPIView,
    RecruiterLoginAPIView,
    RecruiterLogoutAPIView,
    RecruiterForgotPasswordAPIView,
    RecruiterForgotPasswordOTPVerifyAPIView,
    RecruiterResetPasswordAPIView,
    RecruiterProfileAPIView,
    RecruiterHeaderProfileAPIView,
)

app_name = "recruiters"

urlpatterns = [
    path(
        "signup/",
        RecruiterSignupAPIView.as_view(),
        name="signup",
    ),
    path(
        "signup/verify-otp/",
        RecruiterSignupOTPVerifyAPIView.as_view(),
        name="signup-verify-otp",
    ),
    path(
        "login/",
        RecruiterLoginAPIView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        RecruiterLogoutAPIView.as_view(),
        name="logout",
    ),
    path(
        "forgot-password/",
        RecruiterForgotPasswordAPIView.as_view(),
        name="forgot-password",
    ),
    path(
        "forgot-password/verify-otp/",
        RecruiterForgotPasswordOTPVerifyAPIView.as_view(),
        name="forgot-password-verify-otp",
    ),
    path(
        "reset-password/",
        RecruiterResetPasswordAPIView.as_view(),
        name="reset-password",
    ),
    path(
        "profile/",
        RecruiterProfileAPIView.as_view(),
        name="profile",
    ),
    path(
        "profile/header/",
        RecruiterHeaderProfileAPIView.as_view(),
        name="profile-header",
    ),
]