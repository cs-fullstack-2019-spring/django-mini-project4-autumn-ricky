from django import forms
from datetime import date
from .models import GameModel, UserModel


# user model bound form
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user_data_account_created', 'user_rank', 'user_fk']

    # validation
    def clean(self):
        # grab all
        cleaned_data = super().clean()
        # import attributes to validate
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        # throw errors
        if password1 != password2:
            raise forms.ValidationError('Passwords Must Match')


# game model bound form
class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ['game_user']

    # age validation
    def clean_game_age_limit(self):
        age_limit = self.cleaned_data['game_age_limit']
        if age_limit > 18:
            raise forms.ValidationError('Age must be 18 or below')
        if age_limit < 5:
            raise forms.ValidationError('Age must be 5 or above')
        return age_limit

    # date made validation
    def clean_game_date_made(self):
        date_made = self.cleaned_data['game_date_made']
        if date.today() < date_made:
            raise forms.ValidationError('This game is not out yet')

        return date_made
