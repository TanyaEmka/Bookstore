from django.db import models
from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter
from django.contrib.auth import models as user_models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=30)
    author_id = models.IntegerField()
    publisher_id = models.IntegerField()
    subgenre_id = models.IntegerField()
    series_id = models.IntegerField()
    rating_id = models.IntegerField()
    status_id = models.IntegerField()
    price = models.IntegerField()
    page_count = models.IntegerField()
    language = models.CharField(max_length=45)
    publish_year = models.IntegerField()
    sale = models.IntegerField()
    age_limit = models.IntegerField()
    ISBN = models.CharField(max_length=45)
    eISBN = models.CharField(max_length=45)
    series_is = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books'


class BookFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Books
        fields = [
            'min_price',
            'max_price'
        ]


class Authors(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=30)
    death_date = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    rating_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'authors'


class Publishers(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    rating_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publishers'


class Ratings(models.Model):
    value = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ratings'


class Statuses(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'statuses'


class Genres(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'genres'


class SubGenres(models.Model):
    name = models.CharField(max_length=50)
    genre_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sub_genres'


class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=15)
    publisher_id = models.IntegerField()
    rating_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'series'


class Carts(models.Model):
    user_id = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carts'


class Orders(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.IntegerField()
    p_date = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'orders'


class OrderGoods(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    order_id = models.IntegerField()
    book_id = models.IntegerField()
    count = models.IntegerField()
    price = models.IntegerField()
    p_date = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'order_goods'


class Manager(models.Model):
    username = models.CharField(max_length=100)
    publisher_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manager'


class ManagerFilter(FilterSet):
    username = AllValuesFilter(field_name='username')

    class Meta:
        model = Manager
        fields = ['username']


class OrderGoodsFilter(FilterSet):
    user_id = NumberFilter(field_name='user_id')
    status = AllValuesFilter(field_name='status')
    book_id = NumberFilter(field_name='book_id')
    username = AllValuesFilter(field_name='username')

    class Meta:
        model = OrderGoods
        fields = ['user_id', 'status', 'book_id', 'username']


class OrdersFilter(FilterSet):
    user_id = NumberFilter(field_name='user_id')
    status = AllValuesFilter(field_name='status')
    username = AllValuesFilter(field_name='username')

    class Meta:
        model = Orders
        fields = ['user_id', 'status', 'username']


class UserFilter(FilterSet):
    username = AllValuesFilter(field_name='username')
    email = AllValuesFilter(field_name='email')
    first_name = AllValuesFilter(field_name='first_name')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']


class CartsBooks(models.Model):
    cart_id = models.IntegerField()
    book_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carts_books'


class CartsBooksFilter(FilterSet):
    cart_id = NumberFilter(field_name='cart_id')

    class Meta:
        model = CartsBooks
        fields = [
            'cart_id',
        ]



