from rest_framework import serializers

from .models import Candidate



# =====================================================
# Candidate Serializer
# =====================================================

class CandidateSerializer(serializers.ModelSerializer):
    """
    Candidate profile serializer
    """


    class Meta:

        model = Candidate

        fields = [

            "id",

            "full_name",

            "email",

            "phone",

            "skills",

            "role",

            "experience",

            "education",

            "location",

            "preferred_job_type",

            "preferred_location",

            "resume_uploaded",

            "is_active",

            "created_at",

            "updated_at",

        ]


        read_only_fields = [

            "id",

            "created_at",

            "updated_at",

        ]



    # ---------------------------------------------
    # Validate Email
    # ---------------------------------------------

    def validate_email(self, value):

        value = value.lower()


        if Candidate.objects.filter(
            email=value
        ).exclude(
            id=self.instance.id if self.instance else None
        ).exists():

            raise serializers.ValidationError(
                "Email already exists."
            )


        return value



    # ---------------------------------------------
    # Validate Skills
    # ---------------------------------------------

    def validate_skills(self, value):

        if not isinstance(
            value,
            list
        ):

            raise serializers.ValidationError(
                "Skills must be a list."
            )


        return [

            str(skill).strip()

            for skill in value

            if skill

        ]



    # ---------------------------------------------
    # Validate Experience
    # ---------------------------------------------

    def validate_experience(self, value):

        if value < 0:

            raise serializers.ValidationError(
                "Experience cannot be negative."
            )


        return value





# =====================================================
# Candidate Profile Serializer
# =====================================================

class CandidateProfileSerializer(
    serializers.ModelSerializer
):
    """
    Used for displaying candidate profile
    """


    skill_count = serializers.SerializerMethodField()



    class Meta:

        model = Candidate


        fields = [

            "id",

            "full_name",

            "email",

            "skills",

            "skill_count",

            "experience",

            "education",

            "location",

            "preferred_job_type",

            "preferred_location",

        ]



    def get_skill_count(self, obj):

        return len(
            obj.skills or []
        )