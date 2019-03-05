from django import forms
from .models import GameModel, UserModel


# game model
class GameForm(forms.ModelForm):
    class Meta:
        # import game model
        model = GameModel
        # user can access all fields
        fields = '__all__'


# user model
class UserForm(forms.ModelForm):
    class Meta:
        # import user model
        model = UserModel
        # user can access all fields EXCEPT the auto populated date created
        exclude = ['date_account_created']
