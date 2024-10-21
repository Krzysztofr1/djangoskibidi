from django.db import models

# Create your models here.
class dziki_klucz(models.Model):
    liczby_na_sterydach=models.FloatField()

class klasa(models.Model):
    tekst=models.CharField(max_length=100)
    liczby=models.IntegerField()
    pole_dziki_klucz= models.ForeignKey(dziki_klucz,on_delete=models.CASCADE)
