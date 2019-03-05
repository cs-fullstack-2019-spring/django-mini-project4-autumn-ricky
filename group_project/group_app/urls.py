from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index/my_games/', views.my_games, name='my_games'),
    path('index/add_game/', views.add_game, name='add_game'),
    path('index/edit_game/', views.edit_game, name='edit_game'),
    path('index/delete_game/', views.delete_game, name='delete_game'),
    path('index/create_user/', views.create_user, name='create_user')

]
