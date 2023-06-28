from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/')
    curriculo = models.FileField(upload_to='curriculos/')


