from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_filter = ('owner', 'title')
    list_display = ('owner', 'title')
