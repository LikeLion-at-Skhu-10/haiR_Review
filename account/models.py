from django.db import models

from django.contrib.auth.models import User
from django.forms import EmailField

# Create your models here.

class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    nickname = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)