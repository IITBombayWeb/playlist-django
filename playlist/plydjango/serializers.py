from rest_framework import serializers
from .models import play_list, song_detail

class songdetailSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = song_detail
        fields = ('id', 'title', 'artists', 'composer','year','album','url')
        extra_kwargs = {'playlist': {'required': False}}
    
    def create(self, validated_data):
        print("I am here5!")
        print(validated_data)
        return song_detail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("I am here6!")
        instance.__dict__.update(**validated_data)
        instance.save()

        return instance

class PlaylistSerializer(serializers.ModelSerializer):
    songdetail = songdetailSerializer(read_only=True, many=True)

    class Meta:
        model = play_list
        fields = "__all__"
        extra_kwargs = {
            'songdetail': { 'read_only': True }
        }

    def get_or_create_song(self, songdetails):
        print("I am here1!")
        print(songdetails)
        songdetail_ids = []
        for songdetail in songdetails:
            songdetail_instance, created = song_detail.objects.get_or_create(pk=songdetail.get('id'), defaults=songdetail)
            songdetail_ids.append(songdetail_instance.pk)
        return songdetail_ids

    def create_or_update_song(self, songdetails):
        print("I am here2!")
        print(songdetails)
        songdetail_ids = []
        for songdetail in songdetails:
            songdetail_instance, created = song_detail.objects.update_or_create(pk=songdetail.get('id'), defaults=songdetail)
            songdetail_ids.append(songdetail_instance.pk)
        return songdetail_ids

    def create(self, validated_data):
        print("I am here3!")
        print(validated_data)
        # songdetail = validated_data.pop('songdetail', [])
        playlist = play_list.objects.create(**validated_data)
        # playlist.songdetail.set(self.get_or_create_song(songdetail))
        return playlist

    def update(self, instance, validated_data):
        print("I am here4!")
        print(validated_data)
        songdetail = validated_data.pop('songdetail', [])
        instance.songdetail.set(self.create_or_update_song(songdetail))
        fields = ['id', 'name']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass
        instance.save()
        return instance


class PlaylistSongMappingSerializer(serializers.ModelSerializer):
    class Meta:
        # ordering = ['map_id']
        model = play_list
        fields = ['id', 'name']
        # model = play_list_songdetail
        # fields = ['id', 'play_list', 'song_detail']

class SonginPlaylistSerializer(serializers.ModelSerializer):
    songdetail = songdetailSerializer(many=True)
    class Meta:
        model = play_list
        fields = '__all__'

