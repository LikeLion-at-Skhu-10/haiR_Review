from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True),
    nickname = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True) 
    p_num = models.IntegerField(null = True) 
    profile_Img= models.ImageField(upload_to='images/', blank = True)

    def __str__(self) : 
        return self.email


