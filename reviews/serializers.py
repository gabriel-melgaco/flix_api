from rest_framework import serializers
from reviews.models import Review
from movies.serializers import MovieSerializer

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'


class ReviewListDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ['id', 'stars', 'comment', 'movie']