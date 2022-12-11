from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Komenda(models.Model):
    name = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    command = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    volume = models.IntegerField(default=1)
    active = models.BooleanField(default=False)
