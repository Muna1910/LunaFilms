# Generated by Django 4.2 on 2023-05-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommendationapp', '0015_movieselection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieselection',
            name='selected_movies',
        ),
        migrations.AddField(
            model_name='movieselection',
            name='imdbid',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='movieselection',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
