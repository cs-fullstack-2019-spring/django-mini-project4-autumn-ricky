# Generated by Django 2.0.6 on 2019-03-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewUserModel',
            new_name='UserModel',
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='game_developer',
            field=models.CharField(default='', max_length=50),
        ),
    ]
