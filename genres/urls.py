from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreListView.as_view(), name='genre_create_list_view'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),
]