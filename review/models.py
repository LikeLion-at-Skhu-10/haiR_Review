from django.db import models
from account.models import User
from django.conf import settings

# Create your models here.


class Blog(models.Model):
    r_title = models.CharField(max_length=200)
    r_body = models.TextField()
    r_name = models.CharField(max_length=20, null = True, blank = True)
    hashtags = models.ManyToManyField('Hashtag', blank = True)
    r_location = models.CharField(max_length=20, null = True, blank = True)
    r_photo = models.ImageField(upload_to='images/', blank = True)
    r_receipt = models.ImageField(upload_to='images/', blank = True)
    r_nickname = models.CharField(max_length=20, null = True, blank = True)
    r_date = models.DateTimeField('data published')
    r_clicks = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, related_name='r_user', on_delete=models.CASCADE, null=True, default='')
    r_like = models.ManyToManyField(User, related_name='r_likes', blank=True)
    r_likes = models.PositiveIntegerField(default=0)
    r_clip = models.ManyToManyField(User, related_name='r_clip', blank=True)
    r_clips = models.PositiveIntegerField(default=0)




    def __str__(self):
        return self.r_title

    @property
    def r_update_counter(self):
        self.r_clicks += 1
        self.save()


class r_comment(models.Model) :

    def __str__(self) :
        return self.text

    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=20)


class Hashtag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name
