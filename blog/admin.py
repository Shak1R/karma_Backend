from django.contrib import admin
# TODO: import models to admin
from .models import Category, Post


# we can change as from .models import *
# * mean all
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_date', 'category']  # TODO: add author
    list_display_links = ['id', 'title', 'published_date', 'category']   # TODO: add author
    search_fields = ['id', 'title', 'published_date', 'category']  # TODO: add author
