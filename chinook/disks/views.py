from re import template
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from chinook.disks.models import disks_album

def index(request):
    album_list = disks_album.objects.order_by('-artist_id')
    context = {'album_list':album_list}
    return render(request, 'disks/index.html', context)

def album(request, album_id):
    album = get_object_or_404(disks_album, pk=album_id)
    return render(request, 'disks/album.html', {'album' : disks_album})
