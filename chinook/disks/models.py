from django.db import models

class disks_artist(models.Model):
    id = models.IntegerField()
    name = models.CharField()

class disks_album(models.Model):
    id = models.IntegerField()
    title = models.CharField()
    artist_id = models.IntegerField()
    
class disks_track(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    miliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.IntegerField()
    album_id = models.IntegerField()
    composer = models.CharField()
    
