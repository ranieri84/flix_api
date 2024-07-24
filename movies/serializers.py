from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)  # apenas leitura pois não existe a entidade no banco

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']  # no model possui o related name, então ele vai procurar o veview cujo objeto está relacionado
        if rate:
            return round(rate, 1)
        return None

    def validate_release_date(self, value):  # validate nome do campo
        if value.year < 1980:
            raise serializers.ValidationError('A data de lançamento não deve ser anterior a 1980')
        return value

    def validate_resume(self, value):  # validate nome do campo
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres')
        return value


class StatsSerializar(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()


class MovieListDetailSerializer(serializers.ModelSerializer):

    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)  # apenas leitura pois não existe a entidade no banco

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']  # no model possui o related name, então ele vai procurar o veview cujo objeto está relacionado
        if rate:
            return round(rate, 1)
        return None

    class Meta:
        model = Movie
        fields = ['id','title','rate','genre','actors','release_date','resume',]


class MovieStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
