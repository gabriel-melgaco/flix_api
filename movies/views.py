from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieStatsSerializer, MovieListDetailSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieStatsView(views.APIView): #além do CRUD, podemos criar views específicas
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(total=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(Avg('stars'))['stars__avg']

        movie_stats = {'total_movies': total_movies,
                    'movies_by_genre': movies_by_genre,
                    'total_reviews': total_reviews,
                    'average_stars': average_stars
                    }
        
        serializer_class = MovieStatsSerializer(data=movie_stats)
        serializer_class.is_valid(raise_exception=True)

        return response.Response(serializer_class.data, status=status.HTTP_200_OK)
