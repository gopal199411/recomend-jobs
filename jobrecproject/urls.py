from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# =====================================================
# API Root View
# =====================================================

def api_root(request):
    """
    Simple API landing page showing available endpoints.
    """

    return JsonResponse(
        {
            "message": "Job Recommendation API",
            "endpoints": {
                "admin": "/admin/",
                "token": "/api/token/",
                "token_refresh": "/api/token/refresh/",
                "candidates": "/api/candidates/",
                "candidate_register": "/api/candidates/register/",
                "resumes": "/api/resumes/",
                "resume_upload": "/api/resumes/upload/",
                "job_descriptions": "/api/job-descriptions/",
                "recommendations": "/api/recommendations/",
                "generate_recommendations": "/api/recommendations/generate/",
            },
        }
    )


urlpatterns = [

    # =====================================================
    # API Root
    # =====================================================
    path(
        "",
        api_root,
        name="api-root",
    ),

    # =====================================================
    # JWT Authentication
    # =====================================================
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # =====================================================
    # Django Admin
    # =====================================================
    path(
        "admin/",
        admin.site.urls,
    ),

    # =====================================================
    # Candidate APIs
    # =====================================================
    path(
        "api/candidates/",
        include("candidate.urls"),
    ),

    # =====================================================
    # Resume APIs
    # =====================================================
    path(
        "api/resumes/",
        include("resume.urls"),
    ),

    # =====================================================
    # Job Description APIs
    # =====================================================
    path(
        "api/job-descriptions/",
        include("job_description.urls"),
    ),

    # =====================================================
    # Recommendation APIs
    # =====================================================
    path(
        "api/recommendations/",
        include("jos_recommend.urls"),
    ),

]


# =====================================================
# Media Files
# =====================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )