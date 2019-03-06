# Generated by Django 2.0.6 on 2019-03-06 00:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(default='', max_length=50)),
                ('game_developer', models.CharField(default='', max_length=50)),
                ('game_age_limit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('password1', models.CharField(default='', max_length=50)),
                ('password2', models.CharField(default='', max_length=50)),
                ('user_data_account_created', models.DateField(default=datetime.date.today)),
                ('user_rank', models.CharField(default='grunt', max_length=50)),
                ('user_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='game_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game_collector_app.UserModel'),
        ),
    ]
