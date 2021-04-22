from django.shortcuts import render
from django.views import generic

from .models import Music, Album


class MusicListView(generic.ListView):
    model = Music


class MusicDetailView(generic.DetailView):
    model = Music


class AlbumListView(generic.ListView):
    model = Album
