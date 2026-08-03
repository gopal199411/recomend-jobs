from django.test import TestCase

from rest_framework.test import APITestCase

from rest_framework import status

from django.urls import reverse


from .models import JobDescription




# =====================================================
# Job Description Model Test
# =====================================================

class JobDescriptionModelTest(TestCase):


    def setUp(self):

        self.job = JobDescription.objects.create(

            title="Python Django Developer",

            company_name="ABC Technologies",

            location="Chennai",

            salary="6 LPA",

            job_type="FULL_TIME",

            status="OPEN",

            minimum_experience=2,

            maximum_experience=5,

            education="B.Tech",

            description=(
                "Looking for Python Django developer "
                "with REST API and SQL skills"
            ),

            required_skills=[

                "Python",

                "Django",

                "SQL"

            ],

            preferred_skills=[

                "Docker",

                "AWS"

            ]

        )



    def test_job_creation(self):

        self.assertEqual(

            self.job.title,

            "Python Django Developer"

        )


        self.assertEqual(

            self.job.company_name,

            "ABC Technologies"

        )



    def test_job_string_method(self):

        self.assertEqual(

            str(self.job),

            "Python Django Developer - ABC Technologies"

        )






# =====================================================
# Job API Tests
# =====================================================

class JobDescriptionAPITest(APITestCase):


    def setUp(self):

        self.job = JobDescription.objects.create(

            title="Django Developer",

            company_name="XYZ Solutions",

            location="Bangalore",

            job_type="FULL_TIME",

            status="OPEN",

            minimum_experience=1,

            description="Django REST API Developer",

            required_skills=[

                "Python",

                "Django"

            ]

        )



    # ---------------------------------
    # GET Job List
    # ---------------------------------

    def test_get_job_list(self):

        url = reverse(
            "job-list-create"
        )


        response = self.client.get(
            url
        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )



    # ---------------------------------
    # CREATE Job
    # ---------------------------------

    def test_create_job(self):


        url = reverse(
            "job-list-create"
        )


        data = {

            "title":
            "Python Developer",


            "company_name":
            "ABC Tech",


            "location":
            "Chennai",


            "job_type":
            "FULL_TIME",


            "minimum_experience":
            2,


            "description":
            "Python backend developer",


            "required_skills":
            [

                "Python",

                "Django"

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



    # ---------------------------------
    # GET Job Detail
    # ---------------------------------

    def test_get_job_detail(self):


        url = reverse(

            "job-detail",

            args=[self.job.id]

        )


        response = self.client.get(

            url

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_200_OK

        )



    # ---------------------------------
    # DELETE Job
    # ---------------------------------

    def test_delete_job(self):


        url = reverse(

            "job-detail",

            args=[self.job.id]

        )


        response = self.client.delete(

            url

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_204_NO_CONTENT

        )