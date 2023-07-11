from django.shortcuts import render
from .models import Webtoon

# Create your views here.
def webtoon_list(request):
    webtoons = Webtoon.objects.all()
    return render(request, 'webtoon/webtoon_list.html', {'webtoons': webtoons})
