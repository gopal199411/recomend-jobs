from django.test import TestCase

from django.urls import reverse

from rest_framework.test import APITestCase

from rest_framework import status

from django.core.files.uploadedfile import SimpleUploadedFile


from candidate.models import Candidate

from .models import Resume




# =====================================================
# Resume Model Test
# =====================================================

class ResumeModelTest(TestCase):


    def setUp(self):

        self.candidate = Candidate.objects.create(

            full_name="Gopal",

            email="gopal@test.com",

            skills=[
                "python",
                "django"
            ]

        )



    def test_resume_creation(self):

        resume = Resume.objects.create(

            candidate=self.candidate,

            skills=[
                "python",
                "sql"
            ]

        )


        self.assertEqual(

            resume.candidate.full_name,

            "Gopal"

        )


        self.assertTrue(

            isinstance(
                resume.skills,
                list
            )

        )





# =====================================================
# Resume Upload API Test
# =====================================================

class ResumeUploadAPITest(APITestCase):


    def setUp(self):

        self.candidate = Candidate.objects.create(

            full_name="Gopal",

            email="gopal@gmail.com"

        )


        self.url = "/api/resume/upload/"



    def test_resume_upload(self):


        file = SimpleUploadedFile(

            "resume.pdf",

            b"Python Django Developer Resume",

            content_type="application/pdf"

        )



        data = {

            "candidate":
            self.candidate.id,

            "resume_file":
            file

        }



        response = self.client.post(

            self.url,

            data,

            format="multipart"

        )



        self.assertEqual(

            response.status_code,

            status.HTTP_201_CREATED

        )



        self.assertIn(

            "resume_id",

            response.data

        )





# =====================================================
# Resume List API Test
# =====================================================

class ResumeListAPITest(APITestCase):


    def setUp(self):

        self.candidate = Candidate.objects.create(

            full_name="Test User",

            email="test@gmail.com"

        )


        Resume.objects.create(

            candidate=self.candidate,

            skills=[
                "python"
            ]

        )



    def test_resume_list(self):


        response = self.client.get(

            "/api/resume/list/"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )





# =====================================================
# Resume Detail API Test
# =====================================================

class ResumeDetailAPITest(APITestCase):


    def setUp(self):

        self.candidate = Candidate.objects.create(

            full_name="Gopal",

            email="detail@gmail.com"

        )


        self.resume = Resume.objects.create(

            candidate=self.candidate,

            skills=[
                "django"
            ]

        )



    def test_resume_detail(self):


        response = self.client.get(

            f"/api/resume/{self.resume.id}/"

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )





# =====================================================
# Parser Update API Test
# =====================================================

class ResumeParserUpdateTest(APITestCase):


    def setUp(self):

        self.candidate = Candidate.objects.create(

            full_name="Parser User",

            email="parser@gmail.com"

        )


        self.resume = Resume.objects.create(

            candidate=self.candidate

        )



    def test_parser_update(self):


        data = {

            "skills":[

                "python",

                "django",

                "sql"

            ],

            "ats_score":85,

            "is_parsed":True

        }



        response = self.client.patch(

            f"/api/resume/parser-update/{self.resume.id}/",

            data,

            format="json"

        )



        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )