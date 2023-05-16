from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm
# from~에서 import~ 를 import 하라


# 사진 목록
def photo_list(request) :
    photos = Photo.objects.all()
    #photos에 Photo model data를 불러와 템플릿으로 전달
    return render(request, 'photo/photo_list.html', {'photos':photos})
    # render : 서버에 보일 수 있게 보낸다
    #   두 번째 파라미터 : templates 폴더 안에 있는 대상을 가리킴
    #   세 번째 파라미터 : template에 전달할 데이터를 Dictionary로 전달
    #                     dictionary의 key는 두 번째 파라미터의 인수에서 사용할 템플릿 변수명이 됨
    #                     value는 전달하는 내용

    #  ** render에는 request(첫 번째 파라미터)와 template name(두 번째 파라미터)을 반드시 적어야 함



# 세부 화면
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo':photo})


# 작성 화면
def photo_post(request):
    #들어온 요청이 POST인지?
    if request.method == "POST":
        #POST가 맞다면

        form = PhotoForm(request.POST)
        #form에 올림

        if form.is_valid():
            #form에 올라갔으면

            photo = form.save(commit=False)
            #save함(중복 저장을 막기 위해 commit은 False)

            photo.save()
            #새로 올리는 사진을 DB에 저장

            return redirect('photo_detail', pk=photo.pk)
            #photo_detail로 자동으로 갈 수 있게, pk = 몇 번째 사진 < 이것을 불러오는 것(redirect)
    else:
        form = PhotoForm()
        #그렇지 않은 경우 form은 PhotoForm
    return render(request, 'photo/photo_post.html', {'form': form})

def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        #instance라는 변수를 만들어서 데이터 선정 후 새로운 Photo라는 내용을 넣는 것
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            #photo = form.save라고 하면 commit을 통해 바로 호출이 되는데
            # 중복 저장이 될 수 있기 떄문에 그것을 방지하고자
            # commit = False를 작성하는 것
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    #들여쓰기 조심하기, python은 들여쓰기에 따라 달라짐
    return render(request, 'photo/photo_post.html', {'form':form})
