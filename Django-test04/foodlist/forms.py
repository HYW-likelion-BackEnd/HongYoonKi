from django import forms
from .models import Food_model

class Foodlist(forms.ModelForm) :
    class Meta:
        model = Food_model
        fields = ('title', 'star', 'where', 'time', 'description')
