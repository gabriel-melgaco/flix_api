from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer, ReviewListDetailSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission

class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListDetailSerializer
        return ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListDetailSerializer
        return ReviewSerializer
