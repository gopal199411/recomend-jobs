# accounts/serializers.py

import re

from django.contrib.auth import (
    authenticate,
    get_user_model
)

from django.contrib.auth.password_validation import (
    validate_password
)

from rest_framework import serializers

from .models import UserRole


User = get_user_model()



# ==================================
# USER PROFILE SERIALIZER
# ==================================

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [
            "id",
            "username",
            "email",
            "role",
            "phone_number",
            "profile_image",
            "is_email_verified",
            "is_phone_verified",
        ]

        read_only_fields = [
            "id",
            "role",
            "is_email_verified",
            "is_phone_verified",
        ]



# ==================================
# REGISTER - SEND OTP VALIDATION
# ==================================

class SignupOTPSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    phone_number = serializers.CharField(
        required=False,
        allow_blank=True
    )

    password = serializers.CharField(
        write_only=True
    )

    confirm_password = serializers.CharField(
        write_only=True
    )


    def validate_email(self, value):

        value = value.lower().strip()

        if User.objects.filter(
            email__iexact=value
        ).exists():

            raise serializers.ValidationError(
                "Email already exists"
            )

        return value



    def validate_username(self, value):

        value = value.strip()

        if User.objects.filter(
            username__iexact=value
        ).exists():

            raise serializers.ValidationError(
                "Username already exists"
            )

        return value



    def validate_password(self, value):

        validate_password(value)

        if len(value) < 8:
            raise serializers.ValidationError(
                "Password minimum 8 characters"
            )

        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "Need uppercase letter"
            )

        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError(
                "Need lowercase letter"
            )

        if not re.search(r"\d", value):
            raise serializers.ValidationError(
                "Need number"
            )

        if not re.search(
            r"[!@#$%^&*]",
            value
        ):
            raise serializers.ValidationError(
                "Need special character"
            )

        return value



    def validate(self, attrs):

        if attrs["password"] != attrs["confirm_password"]:

            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match"
                }
            )

        return attrs



# ==================================
# CREATE USER AFTER OTP VERIFIED
# ==================================

class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )


    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "phone_number",
            "password"
        ]


    def create(self, validated_data):

        user = User.objects.create_user(
            **validated_data
        )

        user.role = UserRole.CANDIDATE

        user.is_email_verified = True

        user.save()

        return user



# ==================================
# VERIFY OTP
# ==================================

class VerifyOTPSerializer(serializers.Serializer):

    email = serializers.EmailField()

    otp = serializers.CharField(
        max_length=6,
        min_length=6
    )



# ==================================
# LOGIN
# ==================================

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(
        write_only=True
    )


    def validate(self, data):

        user = authenticate(
            username=data["username"],
            password=data["password"]
        )


        if not user:

            raise serializers.ValidationError(
                "Invalid username or password"
            )


        if not user.is_active:

            raise serializers.ValidationError(
                "Account disabled"
            )


        data["user"] = user

        return data



# ==================================
# FORGOT PASSWORD - SEND OTP
# ==================================

class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()



    def validate_email(self, value):

        if not User.objects.filter(
            email=value
        ).exists():

            raise serializers.ValidationError(
                "Email not registered"
            )

        return value



# ==================================
# RESET PASSWORD
# ==================================

class ResetPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()

    otp = serializers.CharField(
        max_length=6,
        min_length=6
    )

    new_password = serializers.CharField(
        write_only=True
    )

    confirm_password = serializers.CharField(
        write_only=True
    )


    def validate(self, data):

        if data["new_password"] != data["confirm_password"]:

            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match"
                }
            )


        validate_password(
            data["new_password"]
        )

        return data