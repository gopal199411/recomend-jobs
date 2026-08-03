from django.urls import path

from .views import (
    JobListCreateAPIView,
    JobDetailAPIView,
    OpenJobListAPIView,
    CompanyJobListAPIView,
)


urlpatterns = [

    # =====================================
    # Job List + Create
    # GET  -> All jobs
    # POST -> Create job
    # =====================================

    path(
        "",
        JobListCreateAPIView.as_view(),
        name="jd-list-create"
    ),



    # =====================================
    # Job Detail
    # GET    -> View job
    # PUT    -> Update job
    # PATCH  -> Partial update
    # DELETE -> Delete job
    # =====================================

    path(
        "<int:pk>/",
        JobDetailAPIView.as_view(),
        name="jd-detail"
    ),



    # =====================================
    # Open Jobs
    # GET -> Only OPEN jobs
    # =====================================

    path(
        "open/",
        OpenJobListAPIView.as_view(),
        name="open-jobs"
    ),



    # =====================================
    # Company Based Jobs
    # Example:
    # /api/jobs/company/?company=ABC
    # =====================================

    path(
        "company/",
        CompanyJobListAPIView.as_view(),
        name="company-jobs"
    ),

]