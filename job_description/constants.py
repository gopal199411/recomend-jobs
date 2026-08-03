# =====================================================
# Job Status Constants
# =====================================================

JOB_STATUS_OPEN = "OPEN"

JOB_STATUS_CLOSED = "CLOSED"

JOB_STATUS_EXPIRED = "EXPIRED"



JOB_STATUS_CHOICES = (

    (JOB_STATUS_OPEN, "Open"),

    (JOB_STATUS_CLOSED, "Closed"),

    (JOB_STATUS_EXPIRED, "Expired"),

)





# =====================================================
# Job Type Constants
# =====================================================

JOB_TYPE_FULL_TIME = "FULL_TIME"

JOB_TYPE_PART_TIME = "PART_TIME"

JOB_TYPE_CONTRACT = "CONTRACT"

JOB_TYPE_INTERNSHIP = "INTERNSHIP"

JOB_TYPE_FREELANCE = "FREELANCE"



JOB_TYPE_CHOICES = (

    (JOB_TYPE_FULL_TIME, "Full Time"),

    (JOB_TYPE_PART_TIME, "Part Time"),

    (JOB_TYPE_CONTRACT, "Contract"),

    (JOB_TYPE_INTERNSHIP, "Internship"),

    (JOB_TYPE_FREELANCE, "Freelance"),

)





# =====================================================
# Allowed Resume / JD File Extensions
# =====================================================

ALLOWED_JD_EXTENSIONS = [

    ".pdf",

    ".doc",

    ".docx",

]





# =====================================================
# Skill Matching Constants
# =====================================================

MINIMUM_MATCH_SCORE = 30


FULL_MATCH_SCORE = 100





# =====================================================
# Default Values
# =====================================================

DEFAULT_JOB_TYPE = JOB_TYPE_FULL_TIME


DEFAULT_JOB_STATUS = JOB_STATUS_OPEN


DEFAULT_EXPERIENCE = 0





# =====================================================
# Technical Skill Database
# Used for JD Parser
# =====================================================

TECHNICAL_SKILLS = [

    # Programming Languages

    "python",

    "java",

    "javascript",

    "c++",

    "c#",



    # Backend

    "django",

    "flask",

    "fastapi",

    "node",

    "spring boot",



    # Frontend

    "html",

    "css",

    "react",

    "angular",

    "vue",



    # Database

    "sql",

    "mysql",

    "postgresql",

    "mongodb",

    "oracle",



    # Cloud / DevOps

    "aws",

    "azure",

    "docker",

    "kubernetes",

    "git",

    "github",



    # AI / Data Science

    "machine learning",

    "deep learning",

    "tensorflow",

    "pytorch",

    "pandas",

    "numpy",

]