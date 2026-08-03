from django.urls import path

from .views import (
    CandidateListCreateAPIView,
    CandidateDetailAPIView,
)


urlpatterns = [

    # List all candidates
    # Create new candidate
    path(
        "",
        CandidateListCreateAPIView.as_view(),
        name="candidate-list-create"
    ),


    # Get / Update / Delete candidate
    path(
        "<int:pk>/",
        CandidateDetailAPIView.as_view(),
        name="candidate-detail"
    ),

]