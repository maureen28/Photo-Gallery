from django.db import models

# Create your models here.

class Location(models.Model):
    country = models.CharField(max_length =150)

    def __str__(self):
        return self.country
    class Meta:
        ordering = ['country']
