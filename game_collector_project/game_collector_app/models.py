from django.db import models
from datetime import date
from django.contrib.auth.models import User


# user model
class UserModel(models.Model):
    username = models.CharField(max_length=50, default='')
    password1 = models.CharField(max_length=50, default='')
    # password2 = models.CharField(max_length=50, default='')
    user_data_account_created = models.DateField(default=date.today)
    user_rank = models.CharField(max_length=50, default='grunt')
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


# game model
class GameModel(models.Model):
    game_name = models.CharField(max_length=50, default='')
    game_developer = models.CharField(max_length=50, default='')
    game_age_limit = models.IntegerField(default=0)
    game_date_made = models.DateField(default=date.today)
    game_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.game_name
