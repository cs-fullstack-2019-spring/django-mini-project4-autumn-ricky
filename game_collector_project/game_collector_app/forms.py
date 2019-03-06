from django import forms
from .models import GameModel, UserModel


# user model bound form
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user_data_account_created', 'user_rank', 'user_fk']

    # def clean_password1(self):
    #     password = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if password != password2:
    #         raise forms.ValidationError('Passwords Must Match')
    #
    #     return password


# game model bound form
class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'

    # age validation
    def clean_game_age_limit(self):
        age_limit = self.cleaned_data['game_age_limit']
        if age_limit > 18:
            raise forms.ValidationError('Age must be 18 or below')
        if age_limit < 5:
            raise forms.ValidationError('Age must be 5 or above')
        return age_limit

    # broken validation
    # def clean_game_date_made(self):
    #     date_made = self.cleaned_data['game_date_made']
    #     if date_made > 2019-01-01:
    #         raise forms.ValidationError('This game is too new')
    #     if date_made < 1900-01-01:
    #         raise forms.ValidationError('This game is too old')
