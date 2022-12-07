from django.shortcuts import render
from datetime import date
from books_app.models import Books, CartsBooks, Carts
from django.contrib.auth.models import User
from books_app.models import Authors, Orders, OrderGoods, Manager
from books_app.models import Publishers
from books_app.models import Statuses
from books_app.models import Ratings
from books_app.models import Genres
from books_app.models import SubGenres
from books_app.models import Series
from books_app.models import BookFilter, CartsBooksFilter, OrderGoodsFilter, OrdersFilter, UserFilter, ManagerFilter
from books_app.serializers import BookSerializer, AuthorSerializer, PublisherSerializer
from books_app.serializers import GenreSerializer, SubGenreSerializer, RatingSerializer
from books_app.serializers import StatusSerializer, SeriesSerializer, CartsBooksSerializer, CartsSerializer
from books_app.serializers import OrderGoodsSerializer, OrdersSerializer, CustomUserSerializer, ManagerSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from books_app.permissions import IsAdminOrReadOnly, IsAuthOwner
import django_filters


# Create your views here.
def auth_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("{'status': 'ok'}")
    else:
        return HttpResponse("{'status': 'error', 'error': 'login failed'}")


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth)
        }
        return Response(content)


def GetBooks(request):
    return render(request, 'books.html', {'data': {
        'current_data': date.today(),
        'books1': [
            {'title': 'Book1', 'id': 1},
            {'title': 'Book2', 'id': 2},
            {'title': 'Book3', 'id': 3}
        ],
        'books': Books.objects.all(),
        'publishers': Publishers.objects.all(),
    }})


def GetBook(request, id):
    return render(request, 'book.html', {'data': {
        'current_data': date.today(),
        'id': id,
        'book': Books.objects.filter(id=id)[0],
        'author': Authors.objects.filter(id=Books.objects.filter(id=id)[0].author_id)[0],
        'publisher': Publishers.objects.filter(id=Books.objects.filter(id=id)[0].publisher_id)[0],
        'status': Statuses.objects.filter(id=Books.objects.filter(id=id)[0].status_id)[0],
        'rating': Ratings.objects.filter(id=Books.objects.filter(id=id)[0].rating_id)[0],
        'genre': Genres.objects.filter(id=SubGenres.objects.filter(id=Books.objects.filter(id=id)[0].subgenre_id)[0].genre_id)[0],
        'sub_genre': SubGenres.objects.filter(id=Books.objects.filter(id=id)[0].subgenre_id)[0],
        'series': Series.objects.filter(id=Books.objects.filter(id=id)[0].series_id)[0],
        'series_is': Books.objects.filter(id=id)[0].series_is
    }})

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Books.objects.all().order_by('id')
    serializer_class = BookSerializer  # Сериализатор для модели
    permission_classes = (IsAdminOrReadOnly, )


class BookTitleViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('title')
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly, )


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly, )


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publishers.objects.all().order_by('id')
    serializer_class = PublisherSerializer
    permission_classes = (IsAdminOrReadOnly, )


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all().order_by('id')
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('id')
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly, )


class SubGenreViewSet(viewsets.ModelViewSet):
    queryset = SubGenres.objects.all().order_by('id')
    serializer_class = SubGenreSerializer
    permission_classes = (IsAdminOrReadOnly, )


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Statuses.objects.all().order_by('id')
    serializer_class = StatusSerializer
    permission_classes = (IsAdminOrReadOnly, )


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all().order_by('id')
    serializer_class = SeriesSerializer
    permission_classes = (IsAdminOrReadOnly, )


class BookSearchViewSet(generics.ListCreateAPIView):
    search_fields = ['title', 'language', 'page_count', 'price']
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = BookFilter
    ordering_fields = ['price']
    queryset = Books.objects.all()
    name = 'Books'
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly, )


class OneBookViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class CartsBooksSearchViewSet(generics.ListCreateAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_class = CartsBooksFilter
    queryset = CartsBooks.objects.all()
    name = "Carts-Books"
    serializer_class = CartsBooksSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OneCartBooksViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartsBooksSerializer
    queryset = CartsBooks.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OrderGoodsSearchViewSet(generics.ListCreateAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_class = OrderGoodsFilter
    queryset = OrderGoods.objects.all()
    serializer_class = OrderGoodsSerializer
    permission_classes = (IsAuthenticated, )


class OneOrderGoodViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderGoodsSerializer
    queryset = OrderGoods.objects.all()
    permission_classes = (IsAuthenticated, )


class OrdersSearchViewSet(generics.ListCreateAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = OrdersFilter
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthOwner, )


class OneOrderViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = (IsAuthOwner, )


class UserInfoViewSet(generics.ListCreateAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = UserFilter
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthOwner, )


class OneUserInfoViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthOwner, )


class ManagerListViewSet(generics.ListCreateAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = ManagerFilter
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class OneManagerViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = (IsAdminOrReadOnly, )