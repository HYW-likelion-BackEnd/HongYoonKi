from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    #TodoForm이라는 class는 Django의 forms class의 ModelForm을 상속받는다
    class Meta:
        model = Todo
        #model 변수에 Todo를 저장한다
        fields = ( 'title', 'description', 'important' )
        #생성할 때 필요한 필수 정보를 fields에 저장한다

