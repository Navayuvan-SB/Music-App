from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicListView.as_view(), name="musics"),
    path('music/<slug:slug>', views.MusicDetailView.as_view(), name="music-detail"),
    path('albums/', views.AlbumListView.as_view(), name="albums"),
]
