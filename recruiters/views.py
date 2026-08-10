from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .models import RecruiterProfile
from .permissions import IsRecruiter
from .serializers import (
    RecruiterLoginSerializer,
    RecruiterProfileSerializer,
    RecruiterRegisterSerializer,
)


class RecruiterRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RecruiterRegisterSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        profile = serializer.save()

        return Response(
            {
                "success": True,
                "message": "Recruiter registration successful",
                "profile": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class RecruiterLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RecruiterLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(
            request=request,
            username=username,
            password=password,
        )

        if user is None:
            return Response(
                {
                    "success": False,
                    "detail": "Invalid username or password.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user.role != "EMPLOYER":
            return Response(
                {
                    "success": False,
                    "detail": "This account is not a recruiter account.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        try:
            profile = user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "detail": "Recruiter profile not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "success": True,
                "message": "Recruiter login successful.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "recruiter": {
                    "full_name": profile.full_name,
                    "email": profile.email,
                    "role": "Recruiter",
                },
            },
            status=status.HTTP_200_OK,
        )


class RecruiterProfileAPIView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request):
        try:
            profile = request.user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {"detail": "Recruiter profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = RecruiterProfileSerializer(
            profile,
            context={"request": request},
        )

        return Response(
            {
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def patch(self, request):
        try:
            profile = request.user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {"detail": "Recruiter profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = RecruiterProfileSerializer(
            profile,
            data=request.data,
            partial=True,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Recruiter profile updated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class RecruiterHeaderAPIView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request):
        try:
            profile = request.user.recruiter_profile
        except RecruiterProfile.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "detail": "Recruiter profile not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        profile_image = None

        if profile.profile_image:
            profile_image = request.build_absolute_uri(
                profile.profile_image.url
            )

        return Response(
            {
                "success": True,
                "full_name": profile.full_name,
                "role": "Recruiter",
                "profile_image": profile_image,
            },
            status=status.HTTP_200_OK,
        )
