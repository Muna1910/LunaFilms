# Generated by Django 4.2 on 2023-05-14 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommendationapp', '0010_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdbid', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('countries', models.CharField(max_length=200)),
                ('plot_outline', models.CharField(max_length=5000)),
                ('genres', models.CharField(max_length=100)),
                ('happy', models.FloatField()),
                ('angry', models.FloatField()),
                ('sad', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
