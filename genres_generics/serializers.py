from rest_framework import serializers
from genres.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        # com uma lista pode escolher qual campo quer retornar por exe ['name']
        fields = '__all__'