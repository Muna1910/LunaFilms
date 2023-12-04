from django.db import models
from django.contrib.auth.models import AbstractUser


# creating a Custom User if needed in the future
class MovieCustomUser(AbstractUser):
    def to_dict(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }

    class Meta:
        verbose_name_plural = 'User'

class Movie(models.Model):
    imdbid = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    countries = models.CharField(max_length=200)
    plot_outline = models.CharField(max_length=5000)
    genres = models.CharField(max_length=100)
    happy = models.FloatField()
    angry = models.FloatField()
    sad = models.FloatField(blank=True, null=True)
    
    # Convert object to a string
    def __str__(self):
        return self.title 

    # Convert object to dictionary 
    def to_dict(self):
        return{
            'imdbid': self.imdbid,
            'title': self.title,
            'year':self.year,            
            'countries': self.countries,
            'plot_outline': self.plot_outline,
            'genres': self.genres,
            'happy': self.happy,
            'angry': self.angry,
            'sad': self.sad,
        }
    


class MovieSelection(models.Model):
    movieuser = models.IntegerField()
    title = models.CharField(default="",max_length=200)
    imdbid = models.CharField(default= 0, max_length=200)
    def to_dict(self):
        return{
            'id': self.id,
            'movieuser': self.movieuser,
            'imdbid':self.imdbid,
            'title': self.title,
        }