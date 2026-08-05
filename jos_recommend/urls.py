from django.urls import path

from .views import (
    JobRecommendationGenerateAPIView,
    JobRecommendationListAPIView,
    JobRecommendationDetailAPIView,
    JobRecommendationUpdateAPIView,
    JobRecommendationDeleteAPIView,
    RecommendationHistoryAPIView,
)


app_name = "jos_recommend"


urlpatterns = [

    # ==========================================
    # Generate Recommendations
    # POST /api/recommendations/generate/
    # ==========================================
    path(
        "generate/",
        JobRecommendationGenerateAPIView.as_view(),
        name="generate-recommendation",
    ),

    # ==========================================
    # Recommendation List
    # GET /api/recommendations/
    # ==========================================
    path(
        "",
        JobRecommendationListAPIView.as_view(),
        name="recommendation-list",
    ),

    # ==========================================
    # Recommendation Detail
    # GET /api/recommendations/<id>/
    # ==========================================
    path(
        "<int:pk>/",
        JobRecommendationDetailAPIView.as_view(),
        name="recommendation-detail",
    ),

    # ==========================================
    # Update Recommendation Status
    # PATCH /api/recommendations/<id>/update/
    # ==========================================
    path(
        "<int:pk>/update/",
        JobRecommendationUpdateAPIView.as_view(),
        name="recommendation-update",
    ),

    # ==========================================
    # Delete Recommendation
    # DELETE /api/recommendations/<id>/delete/
    # ==========================================
    path(
        "<int:pk>/delete/",
        JobRecommendationDeleteAPIView.as_view(),
        name="recommendation-delete",
    ),

    # ==========================================
    # Logged-in User Recommendation History
    # GET /api/recommendations/history/
    # ==========================================
    path(
        "history/",
        RecommendationHistoryAPIView.as_view(),
        name="recommendation-history",
    ),

]
