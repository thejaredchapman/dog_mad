from django.db import models

# Create your models here.
class Question(models.Model):
    name =  models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.PositiveSmallIntegerField(default=0)
    location = models.CharField(max_length=255, blank=True)
    activity1 = models.CharField(max_length=255, blank=True)
    activity2 = models.CharField(max_length=255, blank=True)
    activity3 = models.CharField(max_length=255, blank=True)
    adjective = models.CharField(max_length=255, blank=True)
    number = models.PositiveSmallIntegerField(default=0)
    number1 = models.PositiveSmallIntegerField(default=0)
    tvShow = models.CharField(max_length=255, blank=True)
    favAspectTV = models.CharField(max_length=255, blank=True)
    favSnack = models.CharField(max_length=255, blank=True)
    religion = models.CharField(max_length=255, blank=True)
    favBev = models.CharField(max_length=255, blank=True)
    favOpeningLine = models.CharField(max_length=255, blank=True)

class Photo(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True, max_length=255)
     
