from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, GameForm, GameModel
from django.contrib.auth.models import User


# render welcome page with login
def index(request):
    return render(request, 'group_app/index.html')


def my_games(request):
    return HttpResponse('test my games')


# render new game form
def add_game(request):
    game_form = GameForm(request.POST or None)
    # pass imported form and model
    context = {
        'game_form': game_form,
    }

    if request.method == 'POST':
        # save will add user info to the model
        # game_fk_var = GameModel.objects.get(user_fk=request.user)
          # save will add user info to the model
         game_form.save()
         return render(request, 'group_app/index.html', context)

    return render(request, 'group_app/index.html',context)


def edit_game(request):
    return None


def delete_game(request):
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
