from django.urls import path
from django.contrib import admin

from . import views

app_name = 'disks'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('<int:album_id>', views.album, name ='album')
]