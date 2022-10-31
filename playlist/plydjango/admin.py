from django.contrib import admin
from plydjango.models import song_detail, SongAdmin,play_list,PlaylistAdmin

admin.site.register(song_detail,SongAdmin)
admin.site.register(play_list,PlaylistAdmin)
