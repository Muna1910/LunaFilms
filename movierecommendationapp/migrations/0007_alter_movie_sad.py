# Generated by Django 4.2 on 2023-05-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommendationapp', '0006_remove_movie_metascore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='sad',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
