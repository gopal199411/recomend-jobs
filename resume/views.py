from django.shortcuts import get_object_or_404

from rest_framework import status, generics
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Resume
from .serializers import (
    ResumeSerializer,
    ResumeUploadSerializer,
    ResumeParsedSerializer,
)
from .parser import parse_resume_data
from .services import update_resume_data


# =====================================================
# Resume Upload API
# =====================================================

class ResumeUploadAPIView(generics.CreateAPIView):
    """
    Upload Resume and Parse
    """

    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        resume = serializer.save()

        try:

            file_path = resume.resume_file.path

            parsed_data = parse_resume_data(file_path)

            resume.extracted_text = parsed_data.get(
                "extracted_text", ""
            )

            resume.summary = parsed_data.get(
                "summary", ""
            )

            resume.skills = parsed_data.get(
                "skills", []
            )

            resume.education = parsed_data.get(
                "education", []
            )

            resume.experience = parsed_data.get(
                "experience", []
            )

            resume.projects = parsed_data.get(
                "projects", []
            )

            resume.certifications = parsed_data.get(
                "certifications", []
            )

            resume.languages = parsed_data.get(
                "languages", []
            )

            resume.resume_type = (
                resume.resume_file.name.split(".")[-1].upper()
            )

            resume.is_parsed = True

            resume.save()

        except Exception as e:

            return Response(
                {
                    "message": "Resume uploaded but parsing failed.",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {
                "message": "Resume uploaded and parsed successfully.",
                "resume_id": resume.id,
                "data": ResumeSerializer(resume).data,
            },
            status=status.HTTP_201_CREATED,
        )


# =====================================================
# Resume List API
# =====================================================

class ResumeListAPIView(ListAPIView):
    """
    Get all resumes
    """

    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


# =====================================================
# Resume Detail API
# =====================================================

class ResumeDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get / Update / Delete Resume
    """

    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


# =====================================================
# Candidate Resume History
# =====================================================

class CandidateResumeListAPIView(ListAPIView):
    """
    Get Candidate Resume History
    """

    serializer_class = ResumeSerializer

    def get_queryset(self):

        candidate_id = self.kwargs.get("candidate_id")

        return Resume.objects.filter(
            candidate_id=candidate_id
        )


# =====================================================
# Parsed Resume Data
# =====================================================

class ResumeParsedAPIView(APIView):
    """
    Get Parsed Resume Data
    """

    def get(self, request, pk):

        resume = get_object_or_404(
            Resume,
            pk=pk
        )

        serializer = ResumeParsedSerializer(
            resume
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# =====================================================
# Update Parsed Resume
# =====================================================

class ResumeParserUpdateAPIView(APIView):
    """
    Update Parsed Resume Data
    """

    def patch(self, request, pk):

        updated_resume = update_resume_data(
            pk,
            request.data
        )

        return Response(
            {
                "message": "Resume updated successfully.",
                "data": ResumeSerializer(
                    updated_resume
                ).data,
            },
            status=status.HTTP_200_OK,
        )