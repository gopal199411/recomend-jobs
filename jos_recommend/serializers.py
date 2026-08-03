from rest_framework import serializers

from candidate.models import Candidate
from resume.models import Resume
from job_description.models import JobDescription
from .models import JobRecommendation

from .validators import (
    validate_experience,
    validate_skills,
    validate_job_title,
    validate_description,
)


# =====================================================
# Candidate Serializer
# =====================================================

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"



# =====================================================
# Resume Serializer
# =====================================================

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"



# =====================================================
# Job Description Serializer
# =====================================================

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = "__all__"

    def validate_title(self, value):
        validate_job_title(value)
        return value

    def validate_description(self, value):
        validate_description(value)
        return value

    def validate_required_skills(self, value):
        validate_skills(value)
        return value

    def validate(self, data):
        min_exp = data.get("minimum_experience")
        max_exp = data.get("maximum_experience")
        if min_exp is not None and max_exp is not None:
            validate_experience(min_exp, max_exp)
        return data



# =====================================================
# Job Recommendation Serializer
# =====================================================

class JobRecommendationRequestSerializer(serializers.Serializer):
    """
    Input serializer for generating job recommendations.
    """

    candidate_id = serializers.IntegerField(required=True)

    skills = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        default=list
    )

    experience = serializers.IntegerField(
        required=False,
        default=0
    )

    education = serializers.CharField(
        required=False,
        allow_blank=True
    )

    preferred_location = serializers.CharField(
        required=False,
        allow_blank=True
    )

    preferred_job_type = serializers.CharField(
        required=False,
        allow_blank=True
    )


class JobRecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for JobRecommendation model.
    """

    candidate_name = serializers.CharField(
        source="candidate.full_name",
        read_only=True
    )

    job_title = serializers.CharField(
        source="job.title",
        read_only=True
    )

    company_name = serializers.CharField(
        source="job.company_name",
        read_only=True
    )

    location = serializers.CharField(
        source="job.location",
        read_only=True
    )

    salary = serializers.CharField(
        source="job.salary",
        read_only=True
    )

    experience_required = serializers.SerializerMethodField()

    class Meta:
        model = JobRecommendation

        fields = [
            "id",
            "candidate",
            "candidate_name",
            "resume",
            "job",
            "job_title",
            "company_name",
            "location",
            "salary",
            "experience_required",
            "match_score",
            "skill_score",
            "experience_score",
            "education_score",
            "location_score",
            "matched_skills",
            "missing_skills",
            "recommendation_reason",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "match_score",
            "skill_score",
            "experience_score",
            "education_score",
            "location_score",
            "matched_skills",
            "missing_skills",
            "recommendation_reason",
            "created_at",
            "updated_at",
        ]

    def get_experience_required(self, obj):
        """
        Returns formatted experience requirement.
        """

        minimum = getattr(obj.job, "minimum_experience", None)

        if minimum is None:
            return ""

        return f"{minimum}+ Years"


class RecommendedJobSerializer(serializers.ModelSerializer):
    """
    Serializer used in recommendation API response.
    """

    job_id = serializers.IntegerField(source="id", read_only=True)

    job_title = serializers.CharField(source="title", read_only=True)

    experience_required = serializers.SerializerMethodField()

    match_score = serializers.FloatField(read_only=True)

    matched_skills = serializers.ListField(
        child=serializers.CharField(),
        read_only=True
    )

    missing_skills = serializers.ListField(
        child=serializers.CharField(),
        read_only=True
    )

    class Meta:
        model = JobDescription

        fields = [
            "job_id",
            "job_title",
            "company_name",
            "location",
            "experience_required",
            "salary",
            "match_score",
            "matched_skills",
            "missing_skills",
        ]

    def get_experience_required(self, obj):
        minimum = getattr(obj, "minimum_experience", None)

        if minimum is None:
            return ""

        return f"{minimum}+ Years"

