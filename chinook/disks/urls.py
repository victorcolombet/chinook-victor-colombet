from django.urls import path
from django.contrib import admin

from . import views

app_name = 'disks'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:album_id>/', views.detail, name ='detail')
]