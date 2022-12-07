from books_app.models import Books, Authors, Publishers, Genres, SubGenres, Statuses, Series, Ratings, Carts, CartsBooks
from books_app.models import Orders, OrderGoods, Manager
from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Books
        # Поля, которые мы сериализуем
        fields = ["id", "title", "author_id", "publisher_id", "subgenre_id", "series_id", "rating_id", "status_id", "price", "page_count", "language", "publish_year", "sale", "age_limit", "ISBN", "eISBN", "series_is", "count"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ["id", "name", "birth_date", "death_date", "description", "rating_id"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = ["id", "name", "description", "rating_id"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ["id", "name"]


class SubGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenres
        fields = ["id", "name", "genre_id"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ["id", "value", "count"]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ["id", "name"]


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ["id", "name", "description", "ISBN", "publisher_id", "rating_id"]


class CartsBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartsBooks
        fields = ["id", "cart_id", "book_id", "count"]


class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = ["id", "user_id", "price"]


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id", "user_id", "username", "count", "price", "p_date", "status"]


class OrderGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderGoods
        fields = ["id", "user_id", "username", "order_id", "book_id", "count", "price", "p_date", "status"]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ["id", "username", "publisher_id"]


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')




