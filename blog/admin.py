from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Author, About, Tag, Post,Contact
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('name',)

@admin.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'created_at')
    list_display_links = ('id', 'full_name')
admin.site.register(Contact)