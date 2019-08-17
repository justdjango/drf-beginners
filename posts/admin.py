from django.contrib import admin
from .models import Author, Post


admin.site.register(Author)
admin.site.register(Post)