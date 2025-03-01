from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Candidate
from .serializers import CandidateSerializer
from .services import search_candidates
from .pagination import CandidatePagination


class CandidateViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Candidate objects.

    Provides standard CRUD operations for Candidate model and
    adds a custom search endpoint to filter candidates by query string.

    Attributes:
        queryset: Default queryset returning all Candidate objects
        serializer_class: Serializer used for Candidate data validation and conversion
        pagination_class: Pagination configuration for list responses
    """

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    pagination_class = CandidatePagination

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        """
        Custom action to search candidates based on a query string.

        Accepts a 'search-key' parameter and returns paginated search results
        matching the query. Returns a 400 error if the search key is missing
        or empty, and a 500 error if an exception occurs during the search.

        Args:
            request: HTTP request object containing query parameters

        Returns:
            Response: Paginated JSON response with matching candidates

        Raises:
            400 Bad Request: If search-key parameter is missing or empty
            500 Internal Server Error: If an error occurs during search
        """
        query = request.query_params.get("search-key", None)
        if query is None or query.strip() == "":
            return Response(
                {
                    "detail": "Query parameter 'search-key' is required and cannot be empty."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            qs = search_candidates(query)
        except Exception as e:
            return Response(
                {"detail": "An error occurred during search.", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # Paginate the results.
        paginator = self.pagination_class()
        paginated_qs = paginator.paginate_queryset(qs, request)
        serializer = self.get_serializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)
