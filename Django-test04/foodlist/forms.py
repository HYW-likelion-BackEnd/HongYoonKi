from django import forms
from .models import list

class Foodlist(forms.ModelForm) :
    class Meta:
        model = list
        fields = ('title', 'star', 'where', 'time', 'description')
