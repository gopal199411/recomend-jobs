from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from candidate.models import Candidate
from job_description.models import JobDescription
from .models import JobRecommendation



# ==========================================
# Job Description API Tests
# ==========================================

class JobDescriptionAPITest(APITestCase):


    def setUp(self):

        self.job = JobDescription.objects.create(

            title="Python Django Developer",

            company_name="ABC Technologies",

            location="Chennai",

            job_type="FULL_TIME",

            minimum_experience=1,

            maximum_experience=3,

            education="B.Tech",

            description=
            "Django developer required",

            required_skills=[

                "Python",

                "Django",

                "REST API",

                "SQL"

            ]

        )



    # --------------------------------------
    # Test Job List API
    # --------------------------------------

    def test_job_list(self):

        url = reverse(
            "job-list-create"
        )


        response = self.client.get(url)


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )



    # --------------------------------------
    # Test Create Job API
    # --------------------------------------

    def test_create_job(self):

        url = reverse(
            "job-list-create"
        )


        data = {

            "title":
            "React Developer",

            "company_name":
            "XYZ Tech",

            "location":
            "Bangalore",

            "job_type":
            "FULL_TIME",

            "minimum_experience":
            1,

            "description":
            "Frontend developer with React experience",

            "required_skills":[

                "React",

                "JavaScript"

            ]

        }


        response = self.client.post(
            url,
            data,
            format="json"
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )



    # --------------------------------------
    # Test Job Detail API
    # --------------------------------------

    def test_job_detail(self):

        url = reverse(
            "job-detail",
            args=[
                self.job.id
            ]
        )


        response = self.client.get(url)


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )



    # --------------------------------------
    # Test Update Job
    # --------------------------------------

    def test_update_job(self):

        url = reverse(
            "job-detail",
            args=[
                self.job.id
            ]
        )


        data = {

            "title":
            "Senior Django Developer"

        }


        response = self.client.patch(
            url,
            data,
            format="json"
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )



    # --------------------------------------
    # Test Delete Job
    # --------------------------------------

    def test_delete_job(self):

        url = reverse(
            "job-detail",
            args=[
                self.job.id
            ]
        )


        response = self.client.delete(url)


        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )



# ==========================================
# Job Recommendation API Tests
# ==========================================

class JobRecommendationAPITest(APITestCase):


    def setUp(self):


        self.candidate = Candidate.objects.create(

            full_name="Gopal",

            email="gopal@test.com",

            skills=["python", "django", "sql"]

        )



        self.job = JobDescription.objects.create(

            title="Django Developer",

            company_name="ABC",

            location="Chennai",

            description=
            "Backend developer",

            required_skills=[

                "python",

                "django",

                "sql"

            ]

        )



    # --------------------------------------
    # Test Recommendation API
    # --------------------------------------

    def test_job_recommendation(self):


        url = reverse(
            "job-recommendation"
        )


        data = {

            "candidate_id":
            self.candidate.id,

            "resume_id":
            None

        }


        response = self.client.post(

            url,

            data,

            format="json"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )

        self.assertIn(
            "recommendations",
            response.data
        )


    # --------------------------------------
    # Test Duplicate Recommendation (No Crash)
    # --------------------------------------

    def test_duplicate_recommendation_no_crash(self):

        """
        Calling the same recommendation API twice
        should NOT raise IntegrityError due to
        unique_together constraint.
        """

        url = reverse(
            "job-recommendation"
        )

        data = {

            "candidate_id":
            self.candidate.id,

            "resume_id":
            None

        }


        # First call
        response1 = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response1.status_code,
            status.HTTP_200_OK
        )


        # Second call (same candidate+job) - should NOT crash
        response2 = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response2.status_code,
            status.HTTP_200_OK
        )

        # Verify recommendation count is still 1
        self.assertEqual(
            JobRecommendation.objects.count(),
            1
        )

