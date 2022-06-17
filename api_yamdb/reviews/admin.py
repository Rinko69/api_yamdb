from django.contrib import admin

from .models import User, Category, Genre, Title, GenreTitle, Review


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitle)
admin.site.register(Review)
