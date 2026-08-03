from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


from .models import Resume

from .serializers import (
    ResumeSerializer,
    ResumeUploadSerializer,
    ResumeParsedSerializer
)

from candidate.models import Candidate



# =====================================================
# Resume Upload API
# =====================================================

class ResumeUploadAPIView(APIView):
    """
    Upload candidate resume
    """

    def post(self, request):

        serializer = ResumeUploadSerializer(
            data=request.data
        )


        if serializer.is_valid():

            resume = serializer.save()


            return Response(
                {
                    "message":
                    "Resume uploaded successfully",

                    "resume_id":
                    resume.id,

                    "data":
                    ResumeSerializer(resume).data
                },

                status=status.HTTP_201_CREATED
            )


        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST

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
# Resume Detail / Update / Delete API
# =====================================================

class ResumeDetailAPIView(
    RetrieveUpdateDestroyAPIView
):
    """
    GET    - Resume details
    PUT    - Update resume
    DELETE - Delete resume
    """

    queryset = Resume.objects.all()

    serializer_class = ResumeSerializer



# =====================================================
# Candidate Resume History API
# =====================================================

class CandidateResumeListAPIView(ListAPIView):
    """
    Get resumes by candidate
    """

    serializer_class = ResumeSerializer


    def get_queryset(self):

        candidate_id = self.kwargs.get(
            "candidate_id"
        )


        return Resume.objects.filter(
            candidate_id=candidate_id
        )



# =====================================================
# Resume Parsed Data API
# =====================================================

class ResumeParsedAPIView(APIView):
    """
    Get AI extracted resume data
    """

    def get(self, request, pk):

        resume = get_object_or_404(
            Resume,
            id=pk
        )


        serializer = ResumeParsedSerializer(
            resume
        )


        return Response(

            serializer.data,

            status=status.HTTP_200_OK

        )



# =====================================================
# Resume Parser Update API
# =====================================================

class ResumeParserUpdateAPIView(APIView):
    """
    Update extracted resume information
    after parsing
    """

    def patch(self, request, pk):

        resume = get_object_or_404(
            Resume,
            id=pk
        )


        resume.extracted_text = request.data.get(
            "extracted_text",
            resume.extracted_text
        )


        resume.skills = request.data.get(
            "skills",
            resume.skills
        )


        resume.education = request.data.get(
            "education",
            resume.education
        )


        resume.experience = request.data.get(
            "experience",
            resume.experience
        )


        resume.projects = request.data.get(
            "projects",
            resume.projects
        )


        resume.certifications = request.data.get(
            "certifications",
            resume.certifications
        )


        resume.languages = request.data.get(
            "languages",
            resume.languages
        )


        resume.ats_score = request.data.get(
            "ats_score",
            resume.ats_score
        )


        resume.is_parsed = True


        resume.save()


        return Response(

            {
                "message":
                "Resume parsed data updated successfully",

                "data":
                ResumeSerializer(resume).data
            },

            status=status.HTTP_200_OK

        )