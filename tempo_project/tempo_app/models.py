from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})' 
    
class Merch(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    image = models.URLField(max_length=250)



