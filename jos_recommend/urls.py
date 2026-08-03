from django.urls import path

from .views import (
    JobListCreateAPIView,
    JobDetailAPIView,
    JobRecommendationListAPIView,
    JobRecommendationDetailAPIView,
    JobRecommendationDeleteAPIView,
    JobRecommendationUpdateAPIView,
    CandidateRecommendationHistoryAPIView,
    SearchRecommendationAPIView,
    JobRecommendationAPIView
)


urlpatterns = [

    # ==========================================
    # Job CRUD API
    # ==========================================

    path(
        "jobs/",
        JobListCreateAPIView.as_view(),
        name="job-list-create"
    ),

    path(
        "jobs/<int:pk>/",
        JobDetailAPIView.as_view(),
        name="job-detail"
    ),


    # ==========================================
    # Job Recommendation List / Detail / CRUD
    # ==========================================

    path(
        "recommendations/",
        JobRecommendationListAPIView.as_view(),
        name="recommendation-list"
    ),

    path(
        "recommendations/<int:pk>/",
        JobRecommendationDetailAPIView.as_view(),
        name="recommendation-detail"
    ),

    path(
        "recommendations/<int:pk>/delete/",
        JobRecommendationDeleteAPIView.as_view(),
        name="recommendation-delete"
    ),

    path(
        "recommendations/<int:pk>/update/",
        JobRecommendationUpdateAPIView.as_view(),
        name="recommendation-update"
    ),


    # ==========================================
    # Candidate Recommendation History
    # ==========================================

    path(
        "candidates/<int:candidate_id>/recommendations/",
        CandidateRecommendationHistoryAPIView.as_view(),
        name="candidate-recommendation-history"
    ),


    # ==========================================
    # Search Recommendations
    # ==========================================

    path(
        "recommendations/search/",
        SearchRecommendationAPIView.as_view(),
        name="recommendation-search"
    ),


    # ==========================================
    # Generate Skill-based Recommendations
    # ==========================================

    path(
        "recommend/",
        JobRecommendationAPIView.as_view(),
        name="job-recommendation"
    ),

]
