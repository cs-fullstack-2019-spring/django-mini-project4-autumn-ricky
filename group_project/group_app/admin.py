from django.contrib import admin
from .models import UserModel, GameModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(GameModel)
