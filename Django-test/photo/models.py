from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title