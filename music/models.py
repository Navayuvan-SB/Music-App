from django.db import models

class Label(models.Model):

    name = models.CharField(max_length=200, verbose_name="Label Company Name")
    founded_date = models.DateField(verbose_name="Founded Date")
    headquarters = models.CharField(max_length=512, verbose_name="Location of Headquarters")

