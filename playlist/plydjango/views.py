import queue
from django import views
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import routers, serializers, viewsets, status
from rest_framework import filters
from rest_framework.response import Response
from .models import Song,play_list,PlaylistSongMapping
from .serializers import SongSerializer,PlaylistSerializer,PlaylistSongMappingSerializer,SonginPlaylistSerializer

class getAllSongs(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class addSong(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['song_id']

    #def post(self, request, pk, format=None):
        #return Response("ok")
 
    """
    def perform_create(self, serializer):
        song = get_object_or_404(Song,id=self.request.data.get('song_id'))
        return serializer.save(song=song)
   
    
    
    def get_queryset(self):
        queryset = Song.objects.filter(song_id = self.kwargs['pk'])
        return queryset
    
    def post(self, request, *args, **kwargs):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            addsong = serializer.save()
            serializer = SongSerializer(addsong)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        data = request.data
        serializer = SongSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            x = [dict(i) for i in serializer.data]
            return Response({'data': x}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    """

class deleteSong(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    """"
    def get_queryset(self):
        queryset = Song.objects.filter(song_id = self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_default == True:
            return Response("Cannot delete default system category", status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        songid = pk
        dsong = Song.objects.filter(song_id=songid)
        serializer = SongSerializer(dsong, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    """

class getAllPlaylist(generics.ListAPIView):
    queryset = play_list.objects.all()
    serializer_class = PlaylistSerializer

class addPlaylist(generics.ListCreateAPIView):
    queryset = play_list.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']

    #def get_queryset(self):
        #queryset = Playlist.objects.filter(playlist_id = self.kwargs['pk'])
        #return queryset
    """
    def post(self, request, *args, **kwargs):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            addplaylist = serializer.save()
            serializer = PlaylistSerializer(addplaylist)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

class deletePlaylist(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'playlist_id'
    queryset = play_list.objects.all()
    serializer_class = PlaylistSerializer
    
    """"
    def get_queryset(self):
        queryset = Playlist.objects.filter(song_id = self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_default == True:
            return Response("Cannot delete default system category", status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    """

class addSongtoPlaylist(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = play_list.objects.prefetch_related(Song)
        return queryset
    serializer_class = SongSerializer
    '''lookup_url_kwarg = 'song_id'
    queryset = Song.objects.get(id=lookup_url_kwarg)
    serializer_class = SongSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['song_id']'''
    """
    def post(self, request, *args, **kwargs):
        serializer = PlaylistSongMappingSerializer(data=request.data)
        if serializer.is_valid():
            addsongtoplaylist = serializer.save()
            serializer = PlaylistSongMappingSerializer(addsongtoplaylist)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

class deleteSongfromPlaylist(generics.DestroyAPIView):
    lookup_url_kwarg = 'map_id'
    queryset = PlaylistSongMapping.objects.all()
    serializer_class = PlaylistSongMappingSerializer

    """
    def get_queryset(self):
        queryset = PlaylistSongMapping.objects.filter(song_id = self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_default == True:
            return Response("Cannot delete default system category", status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    """

class getAllSongFromPlaylist(generics.ListAPIView):
    queryset = PlaylistSongMapping.objects.all()
    serializer_class = PlaylistSongMappingSerializer   
