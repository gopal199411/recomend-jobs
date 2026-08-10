from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from .models import RecruiterProfile


User = get_user_model()

profile_image_upload = serializers.ImageField(
    source="profile_image",
    write_only=True,
    required=False,
)

company_logo_upload = serializers.ImageField(
    source="company_logo",
    write_only=True,
    required=False,
)




class RecruiterProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(
        required=False,
        allow_null=True,
    )

    company_logo = serializers.ImageField(
        required=False,
        allow_null=True,
    )

    class Meta:
        model = RecruiterProfile
        fields = [
            "id",
            "full_name",
            "company_name",
            "designation",
            "email",
            "phone_number",
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
            "id",
            "is_online",
            "last_seen",
            "created_at",
            "updated_at",
        ]


class RecruiterRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    password2 = serializers.CharField(
        write_only=True,
    )

    full_name = serializers.CharField(max_length=150)

    company_name = serializers.CharField(max_length=200)

    designation = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    phone_number = serializers.CharField(
        max_length=15,
        required=False,
        allow_blank=True,
    )

    profile_image = serializers.ImageField(
        required=False,
        allow_null=True,
    )

    company_logo = serializers.ImageField(
        required=False,
        allow_null=True,
    )

    website = serializers.URLField(
        required=False,
        allow_blank=True,
    )

    address = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    city = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    state = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    country = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    bio = serializers.CharField(
        required=False,
        allow_blank=True,
    )

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
            role="EMPLOYER",
        )

        profile, created = RecruiterProfile.objects.update_or_create(
            user=user,
            defaults={
                "email": email,
                **validated_data,
            },
        )

        return profile

    def to_representation(self, instance):
        return RecruiterProfileSerializer(
            instance,
            context=self.context,
        ).data
        
        
        
class RecruiterLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )