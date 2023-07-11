from django.db import models

# Create your models here.
class Food_model (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    star = models.IntegerField(max_length=5)
    where = models.TextField(max_length=200)
    time = models.TextField(max_length=100)

    def __str__(self):
        return self.title
