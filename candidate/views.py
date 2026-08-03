from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny

from .models import Candidate
from .serializers import CandidateSerializer


# =====================================================
# Candidate List + Create API
# =====================================================

class CandidateListCreateAPIView(ListCreateAPIView):
    """
    GET  : List all candidates
    POST : Create new candidate
    """

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [AllowAny]



# =====================================================
# Candidate Detail API
# =====================================================

class CandidateDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    GET    : Candidate detail
    PUT    : Update candidate
    DELETE : Delete candidate
    """

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [AllowAny]
