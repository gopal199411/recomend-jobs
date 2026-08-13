from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers

from .models import RecruiterHeaderProfile, RecruiterProfile

User = get_user_model()


class RecruiterSignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )
    full_name = serializers.CharField(max_length=150)
    recruiter_name = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=True,
    )
    company_name = serializers.CharField(max_length=200)
    designation = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=True,
    )
    phone_number = serializers.CharField(
        max_length=15,
        required=False,
        allow_blank=True,
    )
    company_website = serializers.URLField(required=False, allow_blank=True)
    company_location = serializers.CharField(
        max_length=200,
        required=False,
        allow_blank=True,
    )
    industry_type = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )
    address = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(max_length=100, required=False, allow_blank=True)
    state = serializers.CharField(max_length=100, required=False, allow_blank=True)
    country = serializers.CharField(max_length=100, required=False, allow_blank=True)
    bio = serializers.CharField(required=False, allow_blank=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "This username is already registered."
            )
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password2": "Passwords do not match."}
            )
        validate_password(attrs["password"])
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password2")
        username = validated_data.pop("username")
        email = validated_data.pop("email")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="RECRUITER",
            is_active=False,
        )

        profile = RecruiterProfile.objects.create(
            user=user,
            email=email,
            **validated_data,
        )

        RecruiterHeaderProfile.objects.get_or_create(
            recruiter_profile=profile,
        )

        return user


# Compatibility name for code that still imports RecruiterRegisterSerializer.
RecruiterRegisterSerializer = RecruiterSignupSerializer


class SignupOTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(min_length=6, max_length=6)


class RecruiterLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )


class RecruiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterProfile
        fields = [
            "id",
            "full_name",
            "recruiter_name",
            "email",
            "phone_number",
            "designation",
            "company_name",
            "company_website",
            "company_location",
            "industry_type",
            "address",
            "city",
            "state",
            "country",
            "bio",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class RecruiterHeaderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterHeaderProfile
        fields = [
            "profile_image",
            "company_logo",
            "website",
            "address",
            "city",
            "state",
            "country",
            "bio",
            "is_online",
            "last_seen",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "is_online",
            "last_seen",
            "created_at",
            "updated_at",
        ]


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ForgotPasswordOTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(min_length=6, max_length=6)


class ResetPasswordSerializer(serializers.Serializer):
    reset_token = serializers.UUIDField(write_only=True)
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password2": "Passwords do not match."}
            )
        validate_password(attrs["password"])
        return attrs