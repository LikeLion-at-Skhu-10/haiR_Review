from email.mime import image
from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank =True)
    introduction = models.TextField(blank=True)
    p_image = models.ImageField(upload_to = 'account/images', blank = True)
