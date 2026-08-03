from rest_framework.pagination import PageNumberPagination

from .constants import (
    DEFAULT_PAGE_SIZE,
    MAX_PAGE_SIZE
)



# ==========================================
# Job List Pagination
# ==========================================

class JobPagination(PageNumberPagination):
    """
    Pagination for Job Description list API
    """

    page_size = DEFAULT_PAGE_SIZE

    page_size_query_param = "page_size"

    max_page_size = MAX_PAGE_SIZE



# ==========================================
# Recommendation Pagination
# ==========================================

class RecommendationPagination(
    PageNumberPagination
):
    """
    Pagination for Job Recommendations
    """

    page_size = 5

    page_size_query_param = "limit"

    max_page_size = 20