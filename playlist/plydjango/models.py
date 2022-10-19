from django.db import models
from django.contrib import admin

# Models created

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artists = models.CharField(max_length=200)
    composers = models.CharField(max_length=200)
    year = models.IntegerField()
    album = models.CharField(max_length=100)
    yt_url = models.URLField()

    def __str__(self):
        return "Song" + self.title 

'''class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    playlist_name = models.CharField(max_length=200,unique=True)
    song = models.ManyToManyField('Song',related_name='play',blank=True)

    def __str__(self):
        return "Playlist" + self.playlist_name'''

class play_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    song = models.ManyToManyField('Song',related_name='play',blank=True)

    def __str__(self):
        return "Playlist" + self.name
        

class PlaylistSongMapping(models.Model):
    playlist = models.ForeignKey('plydjango.play_list',on_delete=models.CASCADE)
    song = models.ForeignKey('plydjango.Song',on_delete=models.CASCADE)
    map_id = models.IntegerField() 

    class Meta:
        ordering = ['map_id']

class SongAdmin(admin.ModelAdmin):
    list_display = ['song_id', 'title',
                    'artists',
                    'composers',
                    'year',
                    'album',
                    'yt_url'
                    ]

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','song']
