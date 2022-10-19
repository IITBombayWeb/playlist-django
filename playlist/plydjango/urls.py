from email.mime import base
from django.urls import path
from . import views

from rest_framework.schemas import get_schema_view

from django.views.generic import TemplateView

urlpatterns = [
    path('openapi/', get_schema_view(title="Playlist Service"), name='openapi-schema'),   #description="API developers hpoing to use our service"
    path('api/addSong', views.addSong.as_view()),
    path('api/addPlaylist', views.addPlaylist.as_view()),
    path('api/deleteSong/<int:song_id>', views.deleteSong.as_view()),
    path('api/deletePlaylist/<int:playlist_id>', views.deletePlaylist.as_view()),
    path('api/deletePlaylistSongMapping/<int:playlist_id>/<int:song_id>', views.deleteSongfromPlaylist.as_view()),
    path('api/getAllSongs', views.getAllSongs.as_view()),
    path('api/getAllPlaylist', views.getAllPlaylist.as_view()),
    path('api/addPlaylistSongMapping/<int:playlist_id>/<int:song_id>', views.addSongtoPlaylist.as_view()),
    path('api/getAllPlaylistSongs/<int:playlist_id>', views.getAllSongFromPlaylist.as_view()),
    path('docs', TemplateView.as_view(template_name='documentation.html',extra_context={'schema_url':'openapi-schema'}
                                       ), name='swagger-ui'),
]