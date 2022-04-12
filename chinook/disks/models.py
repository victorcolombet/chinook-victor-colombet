from django.db import models

class disks_artist(models.Model):
    id = models.IntegerField(default = 1, primary_key=True)
    name = models.CharField(max_length=200)

class disks_album(models.Model):
    id = models.IntegerField(default = 1, primary_key=True)
    title = models.CharField(max_length=200)
    artist_id = models.IntegerField(default = 1)
    
class disks_track(models.Model):
    id = models.IntegerField(default = 1, primary_key=True)
    name = models.CharField(max_length=200)
    miliseconds = models.IntegerField(default = 0)
    bytes = models.IntegerField(default = 0)
    unitPrice = models.IntegerField(default = 0)
    album_id = models.IntegerField(default = 0)
    composer = models.CharField(max_length=200)
    
