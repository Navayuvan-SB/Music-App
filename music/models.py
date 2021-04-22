from django.db import models


class Label(models.Model):

    name = models.CharField(max_length=200, verbose_name="Label Company Name")
    founded_date = models.DateField(verbose_name="Founded Date")
    headquarters = models.CharField(
        max_length=512, verbose_name="Location of Headquarters")
    slug = models.SlugField("URL param", default=None, null=True)

    def __str__(self):
        return self.name


class MusicDirector(models.Model):

    name = models.CharField(
        max_length=200, verbose_name="Name of the music director")
    website = models.URLField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13)
    slug = models.SlugField("URL param", default=None, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name="Genre Name")
    slug = models.SlugField(verbose_name="URL Param")

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=200, verbose_name="Album Name")
    subtitle = models.TextField(verbose_name="Description")

    music_director = models.ForeignKey(
        MusicDirector, on_delete=models.SET_NULL, null=True)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    asin = models.CharField(
        max_length=10, verbose_name="Amazon Standard Indentification Number")
    release_date = models.DateField()

    cover_image = models.ImageField(upload_to="music/images", null=True)

    slug = models.SlugField("URL param", default=None, null=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=200, verbose_name="Song Name")
    duration = models.DurationField(verbose_name="Duration of the song")

    music_director = models.ForeignKey(
        MusicDirector, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)

    slug = models.SlugField("URL param")

    def __str__(self):
        return self.name
