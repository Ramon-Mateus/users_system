from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    years_old = models.IntegerField()
        
    def __str__(self):
        return self.name

