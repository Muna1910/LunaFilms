# Generated by Django 4.2 on 2023-05-14 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommendationapp', '0003_remove_movie_fear_remove_movie_surprise_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='keywords',
        ),
    ]
