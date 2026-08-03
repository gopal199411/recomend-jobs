from django.test import TestCase

from rest_framework.test import APITestCase

from rest_framework import status

from .models import Candidate



# =====================================================
# Candidate Model Test
# =====================================================

class CandidateModelTest(TestCase):


    def test_candidate_creation(self):

        candidate = Candidate.objects.create(

            full_name="Gopal",

            email="gopal@test.com",

            skills=[
                "Python",
                "Django"
            ],

            role="CANDIDATE",

            experience=2,

            education="B.Tech",

            location="Chennai"

        )


        self.assertEqual(

            candidate.full_name,

            "Gopal"

        )


        self.assertEqual(

            candidate.email,

            "gopal@test.com"

        )


        self.assertIn(

            "Python",

            candidate.skills

        )



# =====================================================
# Candidate API Tests
# =====================================================

class CandidateAPITest(APITestCase):


    def setUp(self):

        self.candidate_data = {

            "full_name": "Gopal",

            "email": "gopal@gmail.com",

            "phone": "9876543210",

            "skills": [

                "Python",

                "Django",

                "SQL"

            ],

            "role": "CANDIDATE",

            "experience": 2,

            "education": "B.Tech",

            "location": "Chennai",

            "preferred_job_type": "FULL_TIME",

            "preferred_location": "Chennai"

        }


    # ---------------------------------------------
    # Create Candidate Test
    # ---------------------------------------------

    def test_create_candidate(self):

        response = self.client.post(

            "/api/candidates/",

            self.candidate_data,

            format="json"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_201_CREATED

        )


        self.assertEqual(

            response.data["full_name"],

            "Gopal"

        )



    # ---------------------------------------------
    # List Candidate Test
    # ---------------------------------------------

    def test_get_candidates(self):


        Candidate.objects.create(

            full_name="Test User",

            email="test@gmail.com",

            skills=[
                "Python"
            ]

        )


        response = self.client.get(

            "/api/candidates/"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )



    # ---------------------------------------------
    # Detail Candidate Test
    # ---------------------------------------------

    def test_get_candidate_detail(self):


        candidate = Candidate.objects.create(

            full_name="Detail User",

            email="detail@gmail.com"

        )


        response = self.client.get(

            f"/api/candidates/{candidate.id}/"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )


        self.assertEqual(

            response.data["email"],

            "detail@gmail.com"

        )



    # ---------------------------------------------
    # Update Candidate Test
    # ---------------------------------------------

    def test_update_candidate(self):


        candidate = Candidate.objects.create(

            full_name="Old Name",

            email="old@gmail.com"

        )


        response = self.client.patch(

            f"/api/candidates/{candidate.id}/",

            {

                "full_name":"New Name"

            },

            format="json"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )


        self.assertEqual(

            response.data["full_name"],

            "New Name"

        )



    # ---------------------------------------------
    # Delete Candidate Test
    # ---------------------------------------------

    def test_delete_candidate(self):


        candidate = Candidate.objects.create(

            full_name="Delete User",

            email="delete@gmail.com"

        )


        response = self.client.delete(

            f"/api/candidates/{candidate.id}/"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_204_NO_CONTENT

        )