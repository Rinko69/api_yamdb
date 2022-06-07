from django.db.models import Avg
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    """
    При запросе произведений возвращается информация
    о категории и жанре в виде объектов.
    """
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = ('id',
                  'name',
                  'year',
                  'rating',
                  'description',
                  'genre',
                  'category',
                  )
        model = Title

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('score')).get('score__avg')
        if not rating:
            return rating
        return round(rating, 1)


class TitlePostSerializer(serializers.ModelSerializer):
    """
    При запросе произведений возвращается информация
    о категории и жанре в виде значения ее поля slug.
    """
    category = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug', queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        fields = ('id',
                  'name',
                  'year',
                  'description',
                  'genre',
                  'category',
                  )
        model = Title
