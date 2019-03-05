from django.db import models
from django.contrib.auth.models import User
from datetime import date


# User Model
class UserModel(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(default=0, max_length=50)
    password2 = models.CharField(default=0, max_length=50)
    date_account_created = models.DateField(default=date.today)
    rank = models.CharField(default="grunt", max_length=50)
    # user model foreign key
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True),

    def __str__(self):
        return self.username


# Game model
class GameModel(models.Model):
    game_name = models.CharField(max_length=50)
    game_developer = models.CharField(max_length=50, default='')
    game_dateMade = models.DateField(default=date.today),
    game_ageLimit = models.IntegerField(default=0)
    # game model foreign key
    game_fk = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True),

    def __str__(self):
        return self.game_name
