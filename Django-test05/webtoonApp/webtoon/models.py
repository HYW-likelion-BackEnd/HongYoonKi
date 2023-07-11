from django.db import models

# Create your models here.

class Webtoon(models.Model) :
    image = models.CharField(max_length=8000)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(default=0)
    keep = models.BooleanField(default=False)

def __str__(self):
    return self.title


