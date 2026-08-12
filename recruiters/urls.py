<<<<<<< HEAD
# recruiters/urls.py

from django.urls import path

from .views import (
    RecruiterRegisterAPIView,
    RecruiterLoginAPIView,
    RecruiterProfileAPIView,
    RecruiterHeaderAPIView,
)


app_name = "recruiters"


urlpatterns = [

    # ==================================
    # RECRUITER REGISTER
    # ==================================

    path(
        "register/",
        RecruiterRegisterAPIView.as_view(),
        name="register",
    ),


    # ==================================
    # RECRUITER LOGIN
    # ==================================

=======
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
    # Signup and email verification
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

    # Login and logout
>>>>>>> e2ad693 (commit msg)
    path(
        "login/",
        RecruiterLoginAPIView.as_view(),
        name="login",
    ),
<<<<<<< HEAD


    # ==================================
    # RECRUITER PROFILE
    # ==================================

=======
    path(
        "logout/",
        RecruiterLogoutAPIView.as_view(),
        name="logout",
    ),

    # Forgot password
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

    # Recruiter profile
>>>>>>> e2ad693 (commit msg)
    path(
        "profile/",
        RecruiterProfileAPIView.as_view(),
        name="profile",
    ),

<<<<<<< HEAD

    # ==================================
    # RECRUITER HEADER
    # ==================================

    path(
        "profile/header/",
        RecruiterHeaderAPIView.as_view(),
        name="header",
    ),

]
=======
    # Header profile: name, photo, online status
    path(
        "profile/header/",
        RecruiterHeaderProfileAPIView.as_view(),
        name="profile-header",
    ),
]
>>>>>>> e2ad693 (commit msg)
