from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from disks.models import Album

def index(request):
    album_list = Album.objects.order_by('-artist_id')
    context = {'album_list': album_list}
    return render(request, 'disks/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'disks/detail.html', {'album' : album})
