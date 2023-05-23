from django.db import models

# Create your models here.

class Todo(models.Model) :
    # Django의 Model에서 models를 받아옴
    title = models.CharField(max_length= 100)
    description =models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    #기본값을 complete하지 않은 상태로 두는 것
    important = models.BooleanField(default=False)
    #중요한 것만 체크할 수 있게 기본값을 false로 설정

#python manage.py migrate 하면 git에 저장이 된다

    def __str__(self):
        return self.title
    #self의 title을 return하라는 함수이다