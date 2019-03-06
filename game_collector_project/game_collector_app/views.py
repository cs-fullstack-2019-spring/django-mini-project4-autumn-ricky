from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserModel, GameModel, GameForm
from django.contrib.auth.models import User


# render welcome page
def index(request):
    return render(request, 'game_collector_app/index.html')


# render new user form
def new_user(request):
    # import form
    new_user_form = UserForm(request.POST or None)
    context = {
        'new_user_form': new_user_form
    }
    # on submit add user to user model and django admin user
    if request.method == 'POST':
        # add to django admin user
        User.objects.create_user(request.POST["username"], " ", request.POST["password1"])

        # add to user model with django admin user foreign key (broken)
        # instance = new_user_form.save(commit=False)
        # instance.user_fk = request.user
        # instance.save()

        # add user to model
        new_user_form.save()
        return render(request, 'game_collector_app/index.html')
    # on load render blank form
    return render(request, 'game_collector_app/new_user.html', context)


# render content for user
def my_page(request):
    # get items in game model by foreign key (broken)
    # current_user = UserModel.objects.get(username=request.user)
    # my_games = GameModel.objects.filter(game_user=current_user.username)

    # get all games
    my_games = GameModel.objects.all()
    context = {
        'my_games': my_games
    }
    # render user page
    return render(request, 'game_collector_app/my_page.html', context)


# add game with game form
def add_game(request):
    # import form
    new_game_form = GameForm(request.POST or None)
    context = {
        'new_game_form': new_game_form
    }
    # on submit add game to model and render user page
    if request.method == 'POST':

        # add game to model with fk automatic (broken)
        # instance = new_game_form.save(commit=False)
        # instance.game_user = request.user
        # instance.save()

        # validation
        if new_game_form.is_valid():
            # add game to model
            new_game_form.save()
            # render user page
            return redirect('my_page')
        else:
            context = {
                'new_game_form': new_game_form,
                'errors': new_game_form.errors,
            }
            return render(request, 'game_collector_app/new_game.html', context)

    # on load render blank form
    return render(request, 'game_collector_app/new_game.html', context)


# delete game based on ID
def delete_game(request, id):
    # get game by id
    game_item = get_object_or_404(GameModel, pk=id)
    # on submit delete game and render user page
    if request.method == 'POST':
        # delete game
        game_item.delete()
        # render user page
        return redirect('my_page')
    context = {
        'delete_game': game_item
    }
    # render delete form
    return render(request, 'game_collector_app/delete_game.html', context)


# edit game based on ID with game form
def edit_game(request, id):
    # get game by id
    game_item = get_object_or_404(GameModel, pk=id)
    # import form and populate with game by id
    edit_form = GameForm(request.POST or None, instance=game_item)
    # with validation save game info and render user page
    if edit_form.is_valid():
        # save game
        edit_form.save()
        # render user page
        return redirect('my_page')
    context = {
        'new_game_form': edit_form
    }
    # on load render populated form
    return render(request, 'game_collector_app/new_game.html', context)
