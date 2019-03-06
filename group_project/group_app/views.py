from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UserForm, GameForm, GameModel, UserModel
from django.contrib.auth.models import User


# render welcome page with login
def index(request):
    return render(request, 'group_app/index.html')

# function for games
def my_games(request):
    games = GameModel.objects.all()
    context = {
        'games': games
    }
    return render(request, 'group_app/index.html', context)


# render new game form
def add_game(request):
    game_form = GameForm(request.POST or None)
    # pass imported form and model
    context = {
        'game_form': game_form,
    }

    if request.method == 'POST':
        game_form.save()
        return render(request, 'group_app/index.html', context)

    return render(request, 'group_app/index.html', context)

# function for user to make edit
def edit_game(request, id):
    game_item = get_object_or_404(GameModel, pk=id)
    edit_form = GameForm(request.POST or None, instance=game_item)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    context = {
        'form': edit_form
    }
    return render(request, 'group_app/index.html', context)


def delete_game(request, id):
    return None


# render create user form
def create_user(request):
    # pass imported form
    new_user_form = UserForm(request.POST or None)
    context = {
        'new_user_form': new_user_form
    }

    if request.method == 'POST':
        # create user adds user info to the django user database
        User.objects.create_user(request.POST["username"], " ", request.POST["password1"])
        # save will add user info to the model
        new_user_form.save()
        return render(request, 'group_app/index.html', context)

    return render(request, 'group_app/index.html', context)
