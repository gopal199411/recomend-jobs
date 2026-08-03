from rest_framework import serializers

from .models import JobDescription



# =====================================================
# Job Description Serializer
# =====================================================

class JobDescriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for Job Description CRUD API
    """


    class Meta:

        model = JobDescription


        fields = [

            "id",

            "title",

            "company_name",

            "location",

            "salary",

            "job_type",

            "status",

            "minimum_experience",

            "maximum_experience",

            "education",

            "description",

            "jd_file",

            "extracted_text",

            "required_skills",

            "preferred_skills",

            "experience_keywords",

            "responsibilities",

            "qualifications",

            "created_at",

            "updated_at",

        ]


        read_only_fields = [

            "id",

            "extracted_text",

            "created_at",

            "updated_at",

        ]



    # =================================================
    # Validate Job Title
    # =================================================

    def validate_title(self, value):

        if not value.strip():

            raise serializers.ValidationError(
                "Job title cannot be empty."
            )


        return value.strip()



    # =================================================
    # Validate Company Name
    # =================================================

    def validate_company_name(self, value):

        if not value.strip():

            raise serializers.ValidationError(
                "Company name cannot be empty."
            )


        return value.strip()



    # =================================================
    # Validate Required Skills
    # =================================================

    def validate_required_skills(self, value):

        if not isinstance(value, list):

            raise serializers.ValidationError(
                "Required skills must be a list."
            )


        return [

            str(skill).strip()

            for skill in value

            if skill

        ]



    # =================================================
    # Validate Preferred Skills
    # =================================================

    def validate_preferred_skills(self, value):

        if not isinstance(value, list):

            raise serializers.ValidationError(
                "Preferred skills must be a list."
            )


        return [

            str(skill).strip()

            for skill in value

            if skill

        ]



    # =================================================
    # Validate Experience
    # =================================================

    def validate(self, data):

        minimum = data.get(
            "minimum_experience"
        )

        maximum = data.get(
            "maximum_experience"
        )


        if minimum is not None and minimum < 0:

            raise serializers.ValidationError(
                {
                    "minimum_experience":
                    "Experience cannot be negative."
                }
            )


        if maximum is not None and maximum < 0:

            raise serializers.ValidationError(
                {
                    "maximum_experience":
                    "Experience cannot be negative."
                }
            )


        if (
            minimum is not None
            and maximum is not None
            and minimum > maximum
        ):

            raise serializers.ValidationError(
                {
                    "experience":
                    "Minimum experience cannot exceed maximum experience."
                }
            )


        return data



# =====================================================
# Job List Serializer
# =====================================================

class JobListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for job listing
    """


    skill_count = serializers.SerializerMethodField()



    class Meta:

        model = JobDescription


        fields = [

            "id",

            "title",

            "company_name",

            "location",

            "job_type",

            "minimum_experience",

            "required_skills",

            "skill_count",

            "status",

        ]



    def get_skill_count(self, obj):

        return len(
            obj.required_skills or []
        )



# =====================================================
# Job Detail Serializer
# =====================================================

class JobDetailSerializer(serializers.ModelSerializer):
    """
    Detailed Job Description response
    """


    class Meta:

        model = JobDescription


        fields = "__all__"