from django import forms
from .models import GameModel, NewUserModel


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ['game_developer']


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUserModel
        exclude = ['date_account_created']
