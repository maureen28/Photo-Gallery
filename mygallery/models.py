from django.db import models

# Create your models here.

class Location(models.Model):
    country = models.CharField(max_length =150)

    def __str__(self):
        return self.country
    class Meta:
        ordering = ['country']

class Category(models.Model):
    title = models.CharField(max_length = 100, unique=True)

    def __str__(self):
            return self.title

class Image(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

