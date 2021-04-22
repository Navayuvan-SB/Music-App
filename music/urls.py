from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicListView.as_view(), name="musics"),
    path('music/<slug:slug>', views.MusicDetailView.as_view(), name="music-detail"),
    path('albums/', views.AlbumListView.as_view(), name="albums"),
    path('albums/<slug:slug>', views.AlbumDetailView.as_view(), name="album-detail"),
    path('genres/', views.GenreListView.as_view(), name="genres"),
    path('genres/<slug:slug>', views.GenreDetailView.as_view(), name="genre-detail"),
]
