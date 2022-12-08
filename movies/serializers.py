from rest_framework import serializers
from .models import Movie, CategoryRating, MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, allow_null=True)
    rating = serializers.ChoiceField(choices=CategoryRating.choices, default=CategoryRating.G)
    synopsis = serializers.CharField(required=False, allow_null=True)
    added_by  = serializers.SerializerMethodField()
    

    def get_added_by(self, obj):
        user = obj.user.email 
        return user


    def create(self, validated_data):
        movies = Movie.objects.create(**validated_data)

        return movies


class MovieOrderSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    

    def get_title(self, obj):  
        return obj.movie.title

    def get_buyed_by(self, obj):
        return obj.user.email

    
    def create(self, validated_data):
        movie_perm = MovieOrder.objects.create(**validated_data)

        return movie_perm