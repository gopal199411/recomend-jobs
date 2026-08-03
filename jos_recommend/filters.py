import django_filters

from job_description.models import JobDescription


class JobDescriptionFilter(
    django_filters.FilterSet
):
    """
    Job filtering options
    """


    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains"
    )


    company_name = django_filters.CharFilter(
        field_name="company_name",
        lookup_expr="icontains"
    )


    location = django_filters.CharFilter(
        field_name="location",
        lookup_expr="icontains"
    )


    job_type = django_filters.CharFilter(
        field_name="job_type"
    )


    status = django_filters.CharFilter(
        field_name="status"
    )


    min_experience = django_filters.NumberFilter(
        field_name="minimum_experience",
        lookup_expr="gte"
    )


    max_experience = django_filters.NumberFilter(
        field_name="maximum_experience",
        lookup_expr="lte"
    )


    skills = django_filters.CharFilter(
        method="filter_skills"
    )


    def filter_skills(
        self,
        queryset,
        name,
        value
    ):
        """
        Filter jobs based on required skills
        JSONField search
        """

        return queryset.filter(
            required_skills__icontains=value
        )



    class Meta:

        model = JobDescription

        fields = [

            "title",

            "company_name",

            "location",

            "job_type",

            "status",

            "minimum_experience",

            "maximum_experience",

            "skills"

        ]

