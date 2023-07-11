from django.urls import path
from . import views

urlpatterns = [
    path('', views.webtoon_list, name='webtoon_list'),
    path('admin/', admin.site.urls),
]