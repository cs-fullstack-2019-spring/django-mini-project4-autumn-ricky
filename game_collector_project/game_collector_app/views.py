from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserModel, GameModel, GameForm
from django.contrib.auth.models import User


# render welcome page
def index(request):
    # render welcome page
    return render(request, 'game_collector_app/index.html')


# render new user form
def new_user(request):
    # import form
    new_user_form = UserForm(request.POST or None)
    # pass new user page context
    context = {
        # new user form
        'new_user_form': new_user_form
    }
    # on submit add user to user model and django admin user
    if request.method == 'POST':

        # check validation
        if new_user_form.is_valid():
            # add user to django user table
            User.objects.create_user(request.POST["username"], "", request.POST["password1"])
            # add user to model
            new_user_form.save()
            # render login page
            return render(request, 'game_collector_app/index.html')
        else:
            # throw error
            print("There was an error")
    # on load render blank form
    return render(request, 'game_collector_app/new_user.html', context)


# render content for user
def my_page(request):
    # foreign key
    current_user = UserModel.objects.get(username=request.user)
    # get items in game model by foreign key
    my_games = GameModel.objects.filter(game_user=current_user)

    # pass user page context
    context = {
        # foreign key
        'current_user': current_user,
        # game from model
        'my_games': my_games
    }
    # render user page
    return render(request, 'game_collector_app/my_page.html', context)


# add game with game form
def add_game(request):
    # import form
    new_game_form = GameForm(request.POST or None)
    # pass add game page context
    context = {
        # new game form
        'new_game_form': new_game_form
    }
    # on submit add game to model and render user page
    if request.method == 'POST':

        # validation
        if new_game_form.is_valid():
            # grab foreign key
            current_user = UserModel.objects.get(username=request.user)
            # add game to model and pass foreign key/ logged in user
            GameModel.objects.create(game_name=request.POST['game_name'], game_developer=request.POST['game_developer'],
                                     game_age_limit=request.POST['game_age_limit'],
                                     game_date_made=request.POST['game_date_made'],
                                     game_user=current_user)
            # render user page
            return redirect('my_page')
        else:
            # pass new game page context
            context = {
                # new game form
                'new_game_form': new_game_form,
                # form validation errors
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
    # pass delete game page context
    context = {
        # game item
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
    # pass new game page context
    context = {
        # edit game form
        'new_game_form': edit_form
    }
    # on load render populated form
    return render(request, 'game_collector_app/new_game.html', context)
