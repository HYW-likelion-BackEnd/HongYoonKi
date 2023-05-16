from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    #photo list를 불러와서 실행하라는 함수
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    # path ('어디'에 들어갔을 때, 어느 파일.의 어떤 것을 불러오고, 이름 = '이름이다') 로 작성
    path('photo/new/', views.photo_post, name='photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit')
]