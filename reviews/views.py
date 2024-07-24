
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from rest_framework.permissions import IsAuthenticated


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
