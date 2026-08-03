from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)

from rest_framework.permissions import AllowAny

from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend


from .models import JobDescription


from .serializers import (
    JobDescriptionSerializer,
    JobListSerializer,
    JobDetailSerializer
)



# =====================================================
# JOB LIST + CREATE API
# =====================================================

class JobListCreateAPIView(ListCreateAPIView):
    """
    GET  : List all jobs
    POST : Create new job
    """

    queryset = JobDescription.objects.all()

    serializer_class = JobDescriptionSerializer

    permission_classes = [
        AllowAny
    ]

    filter_backends = [

        DjangoFilterBackend,

        SearchFilter,

        OrderingFilter,

    ]


    filterset_fields = [

        "job_type",

        "status",

        "location",

    ]


    search_fields = [

        "title",

        "company_name",

        "description",

        "required_skills",

    ]


    ordering_fields = [

        "created_at",

        "minimum_experience",

    ]





# =====================================================
# JOB DETAIL API
# =====================================================

class JobDetailAPIView(
    RetrieveUpdateDestroyAPIView
):
    """
    GET    : Job detail
    PUT    : Update job
    DELETE : Delete job
    """


    queryset = JobDescription.objects.all()


    serializer_class = JobDetailSerializer


    permission_classes = [

        AllowAny

    ]





# =====================================================
# OPEN JOB LIST API
# =====================================================

class OpenJobListAPIView(ListAPIView):
    """
    Return only open jobs
    """


    serializer_class = JobListSerializer


    permission_classes = [

        AllowAny

    ]



    def get_queryset(self):

        return JobDescription.objects.filter(

            status="OPEN"

        )





# =====================================================
# COMPANY JOB LIST API
# =====================================================

class CompanyJobListAPIView(ListAPIView):
    """
    Get jobs by company
    """

    serializer_class = JobListSerializer


    permission_classes = [

        AllowAny

    ]


    def get_queryset(self):

        company = self.request.query_params.get(
            "company"
        )


        if company:

            return JobDescription.objects.filter(

                company_name__icontains=company

            )


        return JobDescription.objects.all()