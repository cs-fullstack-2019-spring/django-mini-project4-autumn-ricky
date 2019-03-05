from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Game model

class GameModel(models.Model):
    game_name= models.CharField(max_length=50)
    game_developer=models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True),
    game_dateMade= models.DateField(default=date.today),
    game_ageLimit= models.IntegerField(default=0)

    def __str__(self):
        return self.game_name


class NewUserModel(models.Model):
    username=models.CharField(max_length=50)
    password1=models.CharField(default=0,max_length=50)
    password2=models.CharField(default=0, max_length=50)
    date_account_created=models.DateField(default=date.today)
    rank=models.CharField(default="grunt",max_length=50)


    def __str__(self):
        return self.username





