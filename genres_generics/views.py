from rest_framework import generics
from genres.models import Genre
from genres_generics.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from genres_generics.permissions import GenrePermissionClass

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GenrePermissionClass,)

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
