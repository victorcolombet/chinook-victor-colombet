from django.contrib import admin

from .models import disks_album, disks_artist, disks_track

admin.site.register(disks_album)
admin.site.register(disks_artist)
admin.site.register(disks_track)
