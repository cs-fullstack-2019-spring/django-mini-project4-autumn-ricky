from django import forms
from .models import GameModel, UserModel


# game model
class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


# user model
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['date_account_created']
