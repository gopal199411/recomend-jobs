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

    path(
        "login/",
        RecruiterLoginAPIView.as_view(),
        name="login",
    ),


    # ==================================
    # RECRUITER PROFILE
    # ==================================

    path(
        "profile/",
        RecruiterProfileAPIView.as_view(),
        name="profile",
    ),


    # ==================================
    # RECRUITER HEADER
    # ==================================

    path(
        "profile/header/",
        RecruiterHeaderAPIView.as_view(),
        name="header",
    ),

]
