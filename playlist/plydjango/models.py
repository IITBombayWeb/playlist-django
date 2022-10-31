from django.db import models
from django.contrib import admin

# Models created

class song_detail(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artists = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    album = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return "song_detail" + self.title 


class play_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    songdetail = models.ManyToManyField(song_detail,related_name='songs')

    def __str__(self):
        return "Playlist" + self.name
  

class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',
                    'artists',
                    'composer',
                    'year',
                    'album',
                    'url'
                    ]

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','get_songdetails']
    
    def get_songdetails(self, obj):
        return "\n".join([p.id for p in obj.song_detail.all()])
