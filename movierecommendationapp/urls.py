from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('session', views.user_session, name='session'),
    path('register', views.user_register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('movies', views.get_movies, name='movies'),
    path('addmovies', views.add_movies, name='addmovies'),


]