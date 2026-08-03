from job_description.models import JobDescription
from .models import JobRecommendation


def calculate_skill_match(
        candidate_skills,
        job_skills
):
    """
    Calculate skill matching percentage
    """

    candidate_skills = [
        skill.lower().strip()
        for skill in candidate_skills
    ]

    job_skills = [
        skill.lower().strip()
        for skill in job_skills
    ]


    matched_skills = list(
        set(candidate_skills)
        &
        set(job_skills)
    )


    missing_skills = list(
        set(job_skills)
        -
        set(candidate_skills)
    )


    if job_skills:

        match_percentage = int(
            (
                len(matched_skills)
                /
                len(job_skills)
            )
            * 100
        )

    else:

        match_percentage = 0


    return {

        "match_percentage":
        match_percentage,

        "matched_skills":
        matched_skills,

        "missing_skills":
        missing_skills

    }



def recommend_jobs(
        candidate,
        candidate_skills
):
    """
    Generate job recommendations
    """


    jobs = JobDescription.objects.filter(
        status="OPEN"
    )


    recommendations = []


    for job in jobs:


        result = calculate_skill_match(

            candidate_skills,

            job.required_skills

        )


        score = result[
            "match_percentage"
        ]


        # Recommend only suitable jobs

        if score >= 30:


            recommendation = (
                JobRecommendation.objects.create(

                    candidate=candidate,

                    job=job,

                    match_score=score,

                    matched_skills=
                    result[
                        "matched_skills"
                    ],

                    missing_skills=
                    result[
                        "missing_skills"
                    ],

                    status="Recommended"

                )
            )


            recommendations.append({

                "recommendation_id":
                recommendation.id,

                "job_id":
                job.id,

                "job_title":
                job.title,

                "company":
                job.company_name,

                "location":
                job.location,

                "match_percentage":
                score,

                "matched_skills":
                result[
                    "matched_skills"
                ],

                "missing_skills":
                result[
                    "missing_skills"
                ]

            })


    return recommendations

