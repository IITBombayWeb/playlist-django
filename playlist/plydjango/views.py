import queue
from django import views
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from requests import Request, request
from rest_framework import generics
from rest_framework import routers, serializers, viewsets, status
from rest_framework import filters
from rest_framework.response import Response
from .models import play_list,song_detail
from .serializers import PlaylistSerializer,songdetailSerializer, SonginPlaylistSerializer, PlaylistSongMappingSerializer

#class-based serializers has been used (generics)

class getAllSongs(generics.ListAPIView):
    queryset = song_detail.objects.all()
    serializer_class = songdetailSerializer

class addSong(generics.ListCreateAPIView):
    queryset = song_detail.objects.all()
    serializer_class = songdetailSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']

class deleteSong(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    queryset = song_detail.objects.all()
    serializer_class = songdetailSerializer
    
class getAllPlaylist(generics.ListAPIView):
    queryset = play_list.objects.all()
    serializer_class = PlaylistSerializer

class addPlaylist(generics.ListCreateAPIView):
    queryset = play_list.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']

class deletePlaylist(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'id'
    lookup_url_kwarg = 'id'
    # def get_queryset(self):
    #     queryset = play_list.objects.filter(id=self.kwargs['id']).delete()
    #     return queryset
    queryset = play_list.objects.all()
    serializer_class = PlaylistSerializer

    # def perform_destroy(self, instance):
    #     instance.delete_flag = True
    #     instance.save()

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     # make sure to catch 404's below
    #     obj = queryset.get(pk=self.request.user.organisation_id)
    #     self.check_object_permissions(self.request, obj)
    #     return obj

class addSongtoPlaylist(generics.ListCreateAPIView):
    lookup_url_kwarg = 'id'
    # lookup_url_kwarg = 'song_id'
    queryset = play_list.objects.all()
    # queryset = play_list.songdetail.all()
    serializer_class = PlaylistSerializer
    # serializer_class = PlaylistSongMappingSerializer

    def get(self, request: Request):
        print("-- in get --")

    def post(self, request: Request):
        print("-- in post --")
        print("-- request -- ", request)
        print("-- request.POST -- ", request.POST)
        print("-- request pid -- ", request.POST['playlistId'])

        try: 
            print("-- in try --")
            playlistId = request.POST['playlistId']
            songId = request.POST['songId']

            playlist = play_list.objects.get(id=playlistId)
            print("-- playlist --", playlist)

            song = song_detail.objects.get(id=songId)
            print("-- song --", song)

            print("-- adding now -- ")
            print(playlist.songdetail.add(song))
            print("-- song added --")

            playlist.save()
            print("-- save playlist --")

            return JsonResponse({
                'status': "added",
                'message': "song added to playlist"
            })
        except:
            return JsonResponse({
                'status': "failed",
                'message': "song not added to playlist"
            })

class getAllSongFromPlaylist(generics.ListAPIView):
    # lookup_url_kwarg = 'id'
    # # queryset = play_list.objects.get(id=int(lookup_url_kwarg))
    # print("-- in class get songs --")
    # # print(lookup_url_kwarg)
    # queryset = play_list.objects.get(id=18)
    serializer_class = songdetailSerializer

    def get_queryset(self):
        print("-- in get qs --")
        queryset = play_list.objects.get(id=self.kwargs['id']) 
        print("-- qs -- ", queryset)
        return queryset.songdetail.all()

    # not working
    # def get_context_data(self, **kwargs):
    #     print("-- req get -- ")
    #     context = super().get_context_data(**kwargs)
    #     id = self.kwargs['id']
    #     print("-- req get -- ", request.GET)

    #     # lookup_url_kwarg = 'id'
    #     # print("-- lka -- ", lookup_url_kwarg)
    #     # print("-- if -- ", lookup_field)

    #     # queryset = play_list.objects.get(id=request.GET['id'])
    #     print("-- in get --")

class deleteSongfromPlaylist(generics.RetrieveUpdateDestroyAPIView):
    # lookup_url_kwarg = 'id'
    # queryset = play_list.objects.all() 
    # serializer_class = songdetailSerializer

    def delete(self, request, *args, **kwargs):
        try:
            print("\n\n-- delete -- ")
            print("-- self -- ", self)
            print("-- request -- ", request)
            # print("-- request params -- ", request.params)
            print("-- request post -- ", self.request.POST)
            print("-- args -- ", args)
            print("-- kwargs -- ", kwargs)
            # print("-- **kwargs -- ", **kwargs)
            # return self.destroy(self, request, *args, **kwargs)

            playlist = play_list.objects.get(id=self.kwargs['id']) 
            print("-- playlist -- ", playlist)
            print("-- initial pl songs -- ", playlist.songdetail.all())
            song = song_detail.objects.get(id=self.kwargs['song_id'])
            print("-- song -- ", song)
            queryset = playlist.songdetail.remove(song)
            print("-- remove status -- ", song)
            
            return JsonResponse({
                'status': "removed",
                'message': "song deleted from playlist"
            })
            # return song
        except:
            return JsonResponse({
                'status': "failed",
                'message': "song not removed from playlist"
            })

    # def perform_destroy(self, instance):
    #     print("-- perf dest -- ")
    #     print("-- self -- ", self)
    #     print("-- inst --", instance)
    #     # instance.delete_flag = True
    #     # instance.save()
    #     return instance.delete()


