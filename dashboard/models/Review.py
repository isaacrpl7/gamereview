from django.db import models

# Create your models here.
class Review(models.Model):
    number = models.IntegerField("Número", default=0)
    game = models.CharField("Jogo", max_length=100)
    release_date = models.CharField("Data de lançamento", max_length=100)
    price = models.FloatField("Preço", default=0)
    owners = models.CharField("Donos", max_length=100)
    developer = models.CharField("Desenvolvedor", max_length=100)
    publisher = models.CharField("Publicador", max_length=100)
    average_playtime = models.IntegerField("Tempo médio de jogo", default=0)
    median_playtime = models.IntegerField("Tempo mediano de jogo", default=0)
    metascore = models.IntegerField("Metascore", default=0)
