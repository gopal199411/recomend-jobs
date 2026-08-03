from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from candidate.models import Candidate
from job_description.models import JobDescription
from .models import JobRecommendation
from .serializers import (
    JobDescriptionSerializer,
    JobRecommendationSerializer,
    JobRecommendationRequestSerializer,
    RecommendedJobSerializer,
)
from .filters import JobDescriptionFilter
from .pagination import JobPagination, RecommendationPagination


# =====================================================
# JOB CRUD API
# =====================================================


class JobListCreateAPIView(ListCreateAPIView):
    """
    List all jobs with filtering or create a new job.
    """

    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
    pagination_class = JobPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobDescriptionFilter
    permission_classes = [AllowAny]


class JobDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a job posting.
    """

    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
    permission_classes = [AllowAny]


# =====================================================
# JOB RECOMMENDATION LIST / DETAIL / CRUD
# =====================================================


class JobRecommendationListAPIView(ListAPIView):
    """
    List all job recommendations with pagination.
    """

    queryset = JobRecommendation.objects.all()
    serializer_class = JobRecommendationSerializer
    pagination_class = RecommendationPagination
    permission_classes = [AllowAny]


class JobRecommendationDetailAPIView(RetrieveAPIView):
    """
    Retrieve a single job recommendation.
    """

    queryset = JobRecommendation.objects.all()
    serializer_class = JobRecommendationSerializer
    permission_classes = [AllowAny]


class JobRecommendationDeleteAPIView(DestroyAPIView):
    """
    Delete a job recommendation.
    """

    queryset = JobRecommendation.objects.all()
    serializer_class = JobRecommendationSerializer
    permission_classes = [AllowAny]


class JobRecommendationUpdateAPIView(UpdateAPIView):
    """
    Update a job recommendation (e.g. status).
    """

    queryset = JobRecommendation.objects.all()
    serializer_class = JobRecommendationSerializer
    permission_classes = [AllowAny]


# =====================================================
# CANDIDATE RECOMMENDATION HISTORY
# =====================================================


class CandidateRecommendationHistoryAPIView(ListAPIView):
    """
    List all recommendations for a specific candidate.
    """

    serializer_class = JobRecommendationSerializer
    pagination_class = RecommendationPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        candidate_id = self.kwargs.get("candidate_id")
        return JobRecommendation.objects.filter(
            candidate_id=candidate_id
        )


# =====================================================
# SEARCH RECOMMENDATIONS
# =====================================================


class SearchRecommendationAPIView(ListAPIView):
    """
    Search job recommendations by keyword
    (searches job title, company name, and skills).
    """

    serializer_class = JobRecommendationSerializer
    pagination_class = RecommendationPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get("search", "")
        if query:
            return JobRecommendation.objects.filter(
                Q(job__title__icontains=query)
                | Q(job__company_name__icontains=query)
                | Q(matched_skills__icontains=query)
            )
        return JobRecommendation.objects.all()


# =====================================================
# JOB RECOMMENDATION API (Skill-based matching)
# =====================================================


class JobRecommendationAPIView(APIView):
    """
    Candidate skill based job recommendation
    Supports:
      - GET  /api/recommend/?candidate_id=1  -> list recommendations
      - POST /api/recommend/                 -> generate new recommendations
    """

    permission_classes = [AllowAny]


    # --------------------------------------------------
    # GET  – Retrieve existing recommendations
    # --------------------------------------------------

    def get(self, request):
        """
        Return existing recommendations:
        - If ?candidate_id=<id> provided, return recommendations for that candidate
        - Otherwise return all recommendations
        """

        candidate_id = request.query_params.get("candidate_id")

        if candidate_id:
            try:
                candidate_id = int(candidate_id)
            except (ValueError, TypeError):
                return Response(
                    {"error": "Invalid candidate_id. Must be an integer."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            try:
                candidate = Candidate.objects.get(id=candidate_id)
            except Candidate.DoesNotExist:
                return Response(
                    {"error": "Candidate not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            recommendations = JobRecommendation.objects.filter(
                candidate=candidate
            ).select_related("job", "candidate")
        else:
            recommendations = JobRecommendation.objects.select_related(
                "job", "candidate"
            ).all()

        serializer = JobRecommendationSerializer(
            recommendations, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


    # --------------------------------------------------
    # POST – Generate skill-based recommendations
    # --------------------------------------------------

    def post(self, request):

        # ---- Validate input via serializer ----
        serializer = JobRecommendationRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        validated = serializer.validated_data
        candidate_id = validated["candidate_id"]

        # ---- Resolve candidate ----
        try:
            candidate = Candidate.objects.get(id=candidate_id)
        except Candidate.DoesNotExist:
            return Response(
                {"error": "Candidate not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # ---- Resolve skills ----
        candidate_skills = validated.get("skills") or []

        # If no explicit skills provided, fall back to candidate's stored skills
        if not candidate_skills:
            candidate_skills = getattr(candidate, "skills", []) or []

        # Normalise to lowercase
        candidate_skills = [
            str(skill).lower() for skill in candidate_skills if skill
        ]

        # ---- Match against open jobs ----
        jobs = JobDescription.objects.all()
        recommendations = []

        for job in jobs:
            required_skills = job.required_skills or []
            required_skills = [
                str(skill).lower() for skill in required_skills
            ]

            matched_skills = list(
                set(candidate_skills) & set(required_skills)
            )
            missing_skills = list(
                set(required_skills) - set(candidate_skills)
            )

            if required_skills:
                match_percentage = int(
                    (len(matched_skills) / len(required_skills)) * 100
                )
            else:
                match_percentage = 0

            if match_percentage >= 30:
                recommendation, created = (
                    JobRecommendation.objects.update_or_create(
                        candidate=candidate,
                        job=job,
                        defaults={
                            "match_score": match_percentage,
                            "matched_skills": matched_skills,
                            "missing_skills": missing_skills,
                            "status": "Recommended",
                        },
                    )
                )

                recommendations.append(
                    {
                        "recommendation_id": recommendation.id,
                        "job_id": job.id,
                        "job_title": job.title,
                        "company_name": job.company_name,
                        "location": job.location,
                        "match_score": match_percentage,
                        "matched_skills": matched_skills,
                        "missing_skills": missing_skills,
                    }
                )

        return Response(
            {
                "candidate": candidate_id,
                "total_matches": len(recommendations),
                "recommendations": recommendations,
            },
            status=status.HTTP_200_OK,
        )
