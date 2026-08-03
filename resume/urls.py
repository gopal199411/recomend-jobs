from django.urls import path

from .views import (
    ResumeUploadAPIView,
    ResumeListAPIView,
    ResumeDetailAPIView,
    CandidateResumeListAPIView,
    ResumeParsedAPIView,
    ResumeParserUpdateAPIView,
)


urlpatterns = [

    path(
        "upload/",
        ResumeUploadAPIView.as_view()
    ),

    path(
        "list/",
        ResumeListAPIView.as_view()
    ),

    path(
        "<int:pk>/",
        ResumeDetailAPIView.as_view()
    ),

    path(
        "candidate/<int:candidate_id>/",
        CandidateResumeListAPIView.as_view()
    ),

    path(
        "parsed/<int:pk>/",
        ResumeParsedAPIView.as_view()
    ),

    path(
        "parser-update/<int:pk>/",
        ResumeParserUpdateAPIView.as_view()
    ),

]