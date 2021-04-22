from django.shortcuts import render
from django.views import generic

from .models import Music, Album, Genre, Label, MusicDirector


class MusicListView(generic.ListView):
    model = Music


class MusicDetailView(generic.DetailView):
    model = Music


class AlbumListView(generic.ListView):
    model = Album


class AlbumDetailView(generic.DetailView):
    model = Album


class GenreListView(generic.ListView):
    model = Genre


class GenreDetailView(generic.DetailView):
    model = Genre


class LabelListView(generic.ListView):
    model = Label


class LabelDetailView(generic.DetailView):
    model = Label


class MusicDirectorListView(generic.ListView):
    model = MusicDirector


class MusicDirectorDetailView(generic.DetailView):
    model = MusicDirector
