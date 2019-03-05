from django.contrib import admin
from .models import NewUserModel, GameModel
# Register your models here.

admin.site.register(NewUserModel)
admin.site.register(GameModel)