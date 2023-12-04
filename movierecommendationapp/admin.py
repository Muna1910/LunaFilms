from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MovieCustomUser, Movie, MovieSelection

admin.site.register(MovieCustomUser, UserAdmin)
admin.site.register(Movie)
admin.site.register(MovieSelection)

