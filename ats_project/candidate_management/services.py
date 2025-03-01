from django.db.models import Q, Value, IntegerField, Case, When
from functools import reduce
import operator
from .models import Candidate

def search_candidates(query):
    """
    Perform an optimized search for candidates by matching query words against candidate names.

    This function follows these steps:
      1. Trim the input query and ensure it is not empty. If it is empty, return an empty QuerySet.
      2. Split the trimmed query into individual words.
      3. Build a Q object that uses OR conditions to filter candidates whose name contains at least one
         of the query words (case-insensitive).
      4. Annotate each candidate with a 'relevance' score that sums a value of 1 for each query word found
         in the candidate's name.
      5. Filter out candidates with a relevance score of 0 and sort the remaining candidates in descending
         order of relevance.

    Args:
        query (str): The search query string containing words to match against candidate names.

    Returns:
        QuerySet: A Django QuerySet of Candidate objects that match the search criteria,
                  annotated with a 'relevance' field and ordered by relevance in descending order.
    """
    # Trim the query and check if it's empty.
    if not query or not query.strip():
        return Candidate.objects.none()
    
    # Split the trimmed query into words.
    query_words = query.strip().split()
    
    # Build a Q object to match candidates with at least one word.
    filter_q = Q()
    for word in query_words:
        filter_q |= Q(name__icontains=word)
    
    qs = Candidate.objects.filter(filter_q)
    
    # Build annotations for each query word to calculate relevance.
    relevance_annotations = [
        Case(
            When(name__icontains=word, then=Value(1)),
            default=Value(0),
            output_field=IntegerField()
        ) for word in query_words
    ]
    
    if relevance_annotations:
        relevance_score = reduce(operator.add, relevance_annotations)
        qs = qs.annotate(relevance=relevance_score).filter(relevance__gt=0).order_by('-relevance')
    else:
        qs = Candidate.objects.none()
    
    return qs
