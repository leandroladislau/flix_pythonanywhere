from django.urls import path
from genres.views import genre_create_list_view, genre_detail_view
from genres_generics.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
]
