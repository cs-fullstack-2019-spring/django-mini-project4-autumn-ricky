from django.urls import path
from . import views

urlpatterns = [
    # home page with login/new user
    path('', views.index, name='index'),
    # create a new user
    path('newUser/', views.new_user, name='new_user'),
    # user page
    path('myPage/', views.my_page, name='my_page'),
    # add a game
    path('addGame/', views.add_game, name='add_game'),
    # edit a game
    path('editGame/<str:id>', views.edit_game, name='edit_game'),
    # delete a game
    path('deleteGame/<str:id>', views.delete_game, name='delete_game'),
]
