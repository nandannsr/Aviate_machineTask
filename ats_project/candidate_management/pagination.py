from rest_framework.pagination import PageNumberPagination


class CandidatePagination(PageNumberPagination):
    """
    Custom pagination class for Candidate API endpoints.

    Provides configurable pagination for candidate lists with a default
    page size of 10 and a maximum page size of 100.

    Attributes:
        page_size (int): Default number of items per page
        page_size_query_param (str): Query parameter to customize page size
        max_page_size (int): Maximum allowed page size
    """

    page_size = 10  # Default page size
    page_size_query_param = "page_size"
    max_page_size = 100