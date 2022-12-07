"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from books_app import views
from rest_framework import routers

book_title_router = routers.DefaultRouter()
book_title_router.register(r'books_titles', views.BookTitleViewSet)

author_router = routers.DefaultRouter()
author_router.register(r'authors', views.AuthorViewSet)

publisher_router = routers.DefaultRouter()
publisher_router.register(r'publishers', views.PublisherViewSet)

rating_router = routers.DefaultRouter()
rating_router.register(r'ratings', views.RatingViewSet)

status_router = routers.DefaultRouter()
status_router.register(r'statuses', views.StatusViewSet)

series_router = routers.DefaultRouter()
series_router.register(r'series', views.SeriesViewSet)

genre_router = routers.DefaultRouter()
genre_router.register(r'genres', views.GenreViewSet)

subgenre_router = routers.DefaultRouter()
subgenre_router.register(r'subgenres', views.SubGenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.GetBooks),
    path('book/<int:id>/', views.GetBook, name='book_url'),
    path(r'books/', views.BookSearchViewSet.as_view(), name='books'),
    path('books/<int:pk>/', views.OneBookViewSet.as_view(), name='book'),
    path(r'cartsbooks/', views.CartsBooksSearchViewSet.as_view(), name='cartsbooks'),
    path('cartsbooks/<int:pk>/', views.OneCartBooksViewSet.as_view(), name='cartbook'),
    path(r'ordergoods/', views.OrderGoodsSearchViewSet.as_view()),
    path('ordergoods/<int:pk>/', views.OneOrderGoodViewSet.as_view()),
    path(r'orders/', views.OrdersSearchViewSet.as_view()),
    path('orders/<int:pk>/', views.OneOrderViewSet.as_view()),
    path(r'auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.jwt')),
    path(r'userinfo/', views.UserInfoViewSet.as_view(), name="usersinfo"),
    path('userinfo/<int:pk>/', views.OneUserInfoViewSet.as_view(), name="userinfo"),
    path(r'managers/', views.ManagerListViewSet.as_view(), name='managers'),
    path('managers/<int:pk>', views.OneManagerViewSet.as_view(), name='manager'),
    path('', include(book_title_router.urls)),
    path('', include(author_router.urls)),
    path('', include(publisher_router.urls)),
    path('', include(rating_router.urls)),
    path('', include(status_router.urls)),
    path('', include(series_router.urls)),
    path('', include(genre_router.urls)),
    path('', include(subgenre_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
