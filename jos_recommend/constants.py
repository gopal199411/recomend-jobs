# ==========================================
# Job Status Constants
# ==========================================

JOB_STATUS_OPEN = "OPEN"
JOB_STATUS_CLOSED = "CLOSED"
JOB_STATUS_EXPIRED = "EXPIRED"



JOB_STATUS_CHOICES = [
    JOB_STATUS_OPEN,
    JOB_STATUS_CLOSED,
    JOB_STATUS_EXPIRED
]



# ==========================================
# Job Type Constants
# ==========================================

JOB_TYPE_FULL_TIME = "FULL_TIME"
JOB_TYPE_PART_TIME = "PART_TIME"
JOB_TYPE_CONTRACT = "CONTRACT"
JOB_TYPE_INTERNSHIP = "INTERNSHIP"
JOB_TYPE_FREELANCE = "FREELANCE"



JOB_TYPE_CHOICES = [
    JOB_TYPE_FULL_TIME,
    JOB_TYPE_PART_TIME,
    JOB_TYPE_CONTRACT,
    JOB_TYPE_INTERNSHIP,
    JOB_TYPE_FREELANCE
]



# ==========================================
# Recommendation Constants
# ==========================================

MINIMUM_MATCH_SCORE = 30


MAX_RECOMMENDATIONS = 10



# ==========================================
# Recommendation Status
# ==========================================

RECOMMENDATION_STATUS_RECOMMENDED = "Recommended"
RECOMMENDATION_STATUS_APPLIED = "Applied"
RECOMMENDATION_STATUS_REJECTED = "Rejected"
RECOMMENDATION_STATUS_EXPIRED = "Expired"



RECOMMENDATION_STATUS_CHOICES = [

    RECOMMENDATION_STATUS_RECOMMENDED,

    RECOMMENDATION_STATUS_APPLIED,

    RECOMMENDATION_STATUS_REJECTED,

    RECOMMENDATION_STATUS_EXPIRED

]



# ==========================================
# Skill Matching Constants
# ==========================================

SKILL_MATCH_WEIGHT = 0.6

EXPERIENCE_MATCH_WEIGHT = 0.25

EDUCATION_MATCH_WEIGHT = 0.15



# ==========================================
# Default Messages
# ==========================================

JOB_NOT_FOUND = "Job not found"

CANDIDATE_NOT_FOUND = "Candidate not found"

RESUME_NOT_FOUND = "Resume not found"

NO_RECOMMENDATION_FOUND = (
    "No suitable jobs found"
)



# ==========================================
# Pagination Constants
# ==========================================

DEFAULT_PAGE_SIZE = 10

MAX_PAGE_SIZE = 50