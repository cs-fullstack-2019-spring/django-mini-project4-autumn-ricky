from django.contrib import admin
from .models import GameModel, UserModel

# Register your models here.
admin.site.register(GameModel)
admin.site.register(UserModel)
