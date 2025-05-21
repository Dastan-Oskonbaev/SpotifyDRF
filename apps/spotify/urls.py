from django.urls import path, include
from rest_framework import routers

from apps.spotify.views import hello_world, AuthorListApiView, SongDetailApiView, AuthorDetailApiView, \
    AuthorListAPIView, AuthorViewSet, SongViewSet

router = routers.DefaultRouter()
router.register('authors-viewset', AuthorViewSet)
router.register('/song-viewset', SongViewSet)

urlpatterns = [
    path('/hello', hello_world),
    path('author', AuthorListApiView.as_view(), name='author-list'),
    path('song/<int:pk>', SongDetailApiView.as_view(), name='song-detail'),
    path('generics/author/<int:pk>',AuthorDetailApiView.as_view(), name='author-detail'),
    path('generics/authors-list',AuthorListAPIView.as_view(), name='author-list'),
    path('', include(router.urls)),

]