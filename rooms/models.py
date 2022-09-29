from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rooms(models.Model):
    name = models.CharField(max_length=225)
    slug=models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Rooms,related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('date_added',)