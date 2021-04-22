from django.db import models

class Label(models.Model):

    name = models.CharField(max_length=200, verbose_name="Label Company Name")
    founded_date = models.DateField(verbose_name="Founded Date")
    headquarters = models.CharField(max_length=512, verbose_name="Location of Headquarters")


class MusicDirector(models.Model):

    name = models.CharField(max_length=200, verbose_name="Name of the music director")
    website = models.URLField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13)


