from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres_generics.serializers import GenreSerializer
from actors.serializers import ActorSerializer

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    # para incluir validadores personalizados, é necessário sobrescrever o método validate_<nome_do_campo>
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1900')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo deve ter mais que 500 caracteres')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    # Adiciona campo no json movie 
    rate = serializers.SerializerMethodField(read_only = True)
    genre = GenreSerializer()
    actors = ActorSerializer(many = True)

    class Meta:
        model = Movie
        fields = [
                'id',
                'title',
                'genre',
                'actors',
                'release_date',
                'rate',
                'resume',
        ]
    
    # Calcular a função do campo calculado, é necessário criar um método com o nome get_<nome_do_campo>
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None