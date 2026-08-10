# accounts/tests.py

from datetime import timedelta

from django.urls import reverse

from django.contrib.auth import get_user_model

from django.utils import timezone

from rest_framework.test import APITestCase

from rest_framework import status

from .models import OTP, OTPPurpose


User = get_user_model()


class AccountsAPITestCase(APITestCase):

    def test_send_signup_otp(self):
        url = reverse("accounts:send-signup-otp")

        data = {
            "username": "testuser",
            "email": "test@gmail.com",
            "phone_number": "9876543210",
            "password": "Test@12345",
            "confirm_password": "Test@12345",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(
            OTP.objects.filter(
                email="test@gmail.com",
                purpose=OTPPurpose.SIGNUP,
            ).exists()
        )

    def test_verify_signup_otp_creates_user(self):
        OTP.objects.create(
            email="test@gmail.com",
            otp="123456",
            purpose=OTPPurpose.SIGNUP,
            expires_at=timezone.now() + timedelta(minutes=5),
        )

        # Store temporary signup data in session
        session = self.client.session
        session["signup_data"] = {
            "username": "testuser",
            "email": "test@gmail.com",
            "phone_number": "9876543210",
            "password": "Test@12345",
        }
        session.save()

        url = reverse("accounts:verify-signup-otp")

        data = {
            "email": "test@gmail.com",
            "otp": "123456",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            User.objects.filter(username="testuser").exists()
        )

    def test_login_user(self):
        User.objects.create_user(
            username="loginuser",
            email="login@gmail.com",
            password="Test@12345",
        )

        url = reverse("accounts:login")

        data = {
            "username": "loginuser",
            "password": "Test@12345",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("access", response.data)

    def test_profile_without_login(self):
        url = reverse("accounts:profile")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
