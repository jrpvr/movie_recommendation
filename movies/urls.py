from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:movie_id>/', views.like_movie, name='like_movie'),
    path('recommend/', views.recommendations, name='recommendations'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
   path('watchlist/<int:movie_id>/', views.toggle_watchlist, name='toggle_watchlist'),
    path('watchlist/', views.watchlist_page, name='watchlist_page'),
    path('suggest/', views.suggest, name='suggest'),
]