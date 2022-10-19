from rest_framework import serializers
from .models import Song,play_list,PlaylistSongMapping

class SongSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='yt_url')
    composer = serializers.CharField(source='composers')
    class Meta:
        ordering = ['id']
        model = Song
        fields = ('song_id', 'title', 'artists', 'composer','year','album','url')
        extra_kwargs = {'playlist': {'required': False}}
    
    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()

        return instance


class PlaylistSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True, many=True)
    #song = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True)
    class Meta:
        ordering = ['id']
        model = play_list
        fields = ('id','name','song')
        #extra_kwargs = {'song': {'required': False}}

        def to_representation(self, instance):
            rep = super().to_representation(instance)
            rep['song'] = SongSerializer(instance.song.all(), many=True).data
            return rep

    '''def create(self, validate_data):
        songs_data = validate_data.pop('song')
        songs = []
        playlist = play_list.objects.create(**validate_data)
        # for contact_data in contacts_data:
        #     contact = Contact.objects.get(id=contact_data['id'])
        #     contacts.append(contact)
        # validate_data['contacts'] = contacts
        # return course
        for song_data in songs_data:
            print(song_data)
            song_id = songs_data.pop('id')
            print(song_id)
            song = Song.objects.get_or_create(id=song_id, defaults=song_data)

            songs.append(song)

        playlist.song.add(**song)
        return playlist'''


    '''def __init__(self, *args, **kwargs):
        super(play_list, self).__init__(*args, **kwargs)
        self.fields['articles'].queryset = Song.objects.select_related(
            'title'
        ).filter(story_status='fr')'''

'''class Playlistserializer(serializers.Serializer):
    song = SongSerializer(read_only=True,many=True)
    playlist_id = serializers.IntegerField()
    playlist_name = serializers.CharField()'''

class songsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['song_id', 'title', 'artists', 'composers','year','album','yt_url']

class PlaylistSongMappingSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='yt_url')
    class Meta:
        ordering = ['map_id']
        model = PlaylistSongMapping
        fields = '__all__'

class SonginPlaylistSerializer(serializers.ModelSerializer):

    song = songsSerializer(many=True,read_only=True)
    class Meta:
        model = PlaylistSerializer
        fields = ('playlist_id','playlist_name','song')

        read_only_fields = ['playlist_id']

