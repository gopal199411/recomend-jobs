from django.contrib.auth import get_user_model
<<<<<<< HEAD
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

=======
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from rest_framework import serializers

from .models import RecruiterHeaderProfile, RecruiterProfile

User = get_user_model()


class RecruiterSignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
>>>>>>> e2ad693 (commit msg)
    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
        min_length=8,
<<<<<<< HEAD
    )

    password2 = serializers.CharField(
        write_only=True,
    )

    full_name = serializers.CharField(max_length=150)

    company_name = serializers.CharField(max_length=200)

    designation = serializers.CharField(
=======
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
    company_website = serializers.URLField(
        required=False,
        allow_blank=True,
    )
    company_location = serializers.CharField(
        max_length=200,
        required=False,
        allow_blank=True,
    )
    industry_type = serializers.CharField(
>>>>>>> e2ad693 (commit msg)
        max_length=100,
        required=False,
        allow_blank=True,
    )

<<<<<<< HEAD
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

=======
>>>>>>> e2ad693 (commit msg)
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "This username is already registered."
            )
<<<<<<< HEAD

=======
>>>>>>> e2ad693 (commit msg)
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )
<<<<<<< HEAD

=======
>>>>>>> e2ad693 (commit msg)
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password2": "Passwords do not match."}
            )

<<<<<<< HEAD
=======
        validate_password(attrs["password"])
>>>>>>> e2ad693 (commit msg)
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password2")

        username = validated_data.pop("username")
        email = validated_data.pop("email")

<<<<<<< HEAD
=======
        profile_data = {
            "full_name": validated_data.pop("full_name"),
            "company_name": validated_data.pop("company_name"),
            **validated_data,
        }

>>>>>>> e2ad693 (commit msg)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
<<<<<<< HEAD
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
=======
            role="RECRUITER",
            is_active=False,
        )

        profile = RecruiterProfile.objects.create(
            user=user,
            **profile_data,
        )

        RecruiterHeaderProfile.objects.get_or_create(
            recruiter_profile=profile,
        )

        return user


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

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class RecruiterHeaderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterHeaderProfile
        fields = [
            "profile_image",
            "company_logo",
            "is_online",
            "last_seen",
        ]

        read_only_fields = [
            "is_online",
            "last_seen",
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
>>>>>>> e2ad693 (commit msg)
