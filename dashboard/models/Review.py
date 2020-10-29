from django.db import models

# Create your models here.
class Review(models.Model):
    number = models.IntegerField(default=0)
    game = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    owners = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    average_playtime = models.IntegerField(default=0)
    median_playtime = models.IntegerField(default=0)
    metascore = models.IntegerField(default=0)
