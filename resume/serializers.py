from rest_framework import serializers

from .models import Resume



# =====================================================
# Resume Serializer
# =====================================================

class ResumeSerializer(serializers.ModelSerializer):
    """
    Resume upload and detail serializer
    """


    candidate_name = serializers.CharField(
        source="candidate.full_name",
        read_only=True
    )


    class Meta:

        model = Resume

        fields = [

            "id",

            "candidate",
            "candidate_name",

            "resume_file",
            "resume_type",

            "extracted_text",

            "summary",

            "skills",

            "education",

            "experience",

            "projects",

            "certifications",

            "languages",

            "ats_score",

            "is_parsed",

            "created_at",
            "updated_at",
        ]


        read_only_fields = [

            "extracted_text",

            "summary",

            "ats_score",

            "is_parsed",

            "created_at",

            "updated_at",

        ]



# =====================================================
# Resume Upload Serializer
# =====================================================

class ResumeUploadSerializer(serializers.ModelSerializer):
    """
    Used only for resume file upload
    """


    class Meta:

        model = Resume

        fields = [

            "candidate",

            "resume_file",

        ]



    def validate_resume_file(self, value):

        allowed_extensions = [

            "pdf",
            "doc",
            "docx"

        ]


        file_extension = value.name.split(".")[-1].lower()


        if file_extension not in allowed_extensions:

            raise serializers.ValidationError(
                "Only PDF, DOC, DOCX files are allowed."
            )


        return value



# =====================================================
# Resume Parser Response Serializer
# =====================================================

class ResumeParsedSerializer(serializers.ModelSerializer):
    """
    Returns extracted resume information
    """


    class Meta:

        model = Resume

        fields = [

            "id",

            "candidate",

            "summary",

            "skills",

            "education",

            "experience",

            "projects",

            "certifications",

            "languages",

            "ats_score",

            "is_parsed",

        ]