# Generated by Django 4.2 on 2023-05-15 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommendationapp', '0016_remove_movieselection_selected_movies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieselection',
            name='imdbid',
        ),
    ]