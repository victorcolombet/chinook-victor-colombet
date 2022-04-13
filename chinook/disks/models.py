from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
class Track(models.Model):
    name = models.CharField(max_length=200)
    milliseconds = models.IntegerField(default = 0)
    bytes = models.IntegerField(default = 0)
    unitPrice = models.IntegerField(default = 0)
    composer = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
