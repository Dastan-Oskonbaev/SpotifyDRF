from rest_framework import status, generics, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.spotify.filters import AuthorFilter
from apps.spotify.models import Author, Song
from apps.spotify.serializers import AuthorSerializer, SongSerializer, AuthorDetailSerializer


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})


class AuthorListApiView(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)


class SongDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Exception:
            return None


    def get(self, request, pk):
        song = self.get_object(pk)
        if song is None:
            return Response({'message': 'Song not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SongSerializer(song)
        return Response(serializer.data)



class AuthorDetailApiView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer



class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'surname']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = AuthorFilter


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
