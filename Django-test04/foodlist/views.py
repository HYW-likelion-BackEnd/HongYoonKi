from django.shortcuts import render, redirect
from .models import Food_model
from .forms import Foodlist

# Create your views here.
def food_list(request):
    lists = Food_model.objects.all()
    return render(request, 'foodlist/list.html', {'lists' : lists })

def food_detail(request, pk):
    food = Food_model.objects.get(id=pk)
    return render(request, 'foodlist/detail.html', {'food' : food})

def food_post(request):
    if request.method == "POST":
        form = Foodlist(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('food_list')
    else:
        form = Foodlist()
    return render(request, 'foodlist/create.html', {'form' : form})