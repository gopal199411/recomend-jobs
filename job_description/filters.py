import django_filters

from .models import JobDescription



# =====================================================
# Job Description Filter
# =====================================================

class JobDescriptionFilter(
    django_filters.FilterSet
):
    """
    Filter jobs based on fields
    """


    # Location search

    location = django_filters.CharFilter(

        field_name="location",

        lookup_expr="icontains"

    )


    # Company search

    company_name = django_filters.CharFilter(

        field_name="company_name",

        lookup_expr="icontains"

    )


    # Job title search

    title = django_filters.CharFilter(

        field_name="title",

        lookup_expr="icontains"

    )


    # Job type

    job_type = django_filters.CharFilter(

        field_name="job_type",

        lookup_expr="iexact"

    )


    # Status

    status = django_filters.CharFilter(

        field_name="status",

        lookup_expr="iexact"

    )


    # Minimum experience greater than

    min_experience = django_filters.NumberFilter(

        field_name="minimum_experience",

        lookup_expr="gte"

    )


    # Maximum experience less than

    max_experience = django_filters.NumberFilter(

        field_name="maximum_experience",

        lookup_expr="lte"

    )



    class Meta:

        model = JobDescription


        fields = [

            "title",

            "company_name",

            "location",

            "job_type",

            "status",

            "min_experience",

            "max_experience",

        ]