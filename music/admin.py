from django.contrib import admin
from .models import Album, Genre, Label, Music, MusicDirector


class MusicInline(admin.TabularInline):
    model = Music

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "music_director")


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "subtitle", "music_director")
    inlines=[MusicInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(MusicDirector)
class MusicDirectorAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "date_of_birth")


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("name", "founded_date", "headquarters")
