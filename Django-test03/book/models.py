from django.db import models

# Create your models here.

class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    #bid 키를 입력해 줘서 책마다 각각의 고유 값을 가져 책이 겹치지 않게 함
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    #가격
    published_date = models.DateField()
    #출간한 날짜
    description = models.TextField()
