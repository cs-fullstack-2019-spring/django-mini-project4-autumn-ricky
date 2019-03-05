from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    # leads to our index function
    path('index/my_games/', views.my_games, name='my_games'),
    # path created for my_games function
    path('index/add_game/', views.add_game, name='add_game'),
    # path created for add_game function
    path('index/edit_game/<int:id>', views.edit_game, name='edit_game'),
    # path created for edit_game function
    path('index/delete_game/', views.delete_game, name='delete_game'),
    # path created for delete_game function
    path('index/create_user/', views.create_user, name='create_user')
    # path created for create_game function

]
