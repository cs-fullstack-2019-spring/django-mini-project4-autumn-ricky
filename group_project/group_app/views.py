from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.



# Create your views here.
def index(request):
    return render(request, 'group_app/index.html')



def my_games(request):
    return None


def add_game(request):
    return None


def edit_game(request):
    return None


def delete_game(request):
    return None


def create_user(request):
    return None
