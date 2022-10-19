from django.contrib import admin
from plydjango.models import Song, SongAdmin

admin.site.register(Song,SongAdmin)
