from django.contrib import admin

# Register your models here.

from apps.spotify.models import *

# admin.site.register(Author)
admin.site.register(Song)

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'surname', 'album_count')
#     list_display_links = ('name', 'album_count')
#     list_filter = ('name', 'surname', 'album_count')
#     search_fields = ('name', 'surname')
#     ordering = ('id', 'name', 'surname')

admin.site.register(Author)
admin.site.register(Proposal)