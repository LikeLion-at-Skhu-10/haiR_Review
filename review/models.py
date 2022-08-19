from django.db import models

# Create your models here.

from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.

class Review(models.Model):
    r_title = models.CharField(max_length=200)
    r_body = models.TextField()
    name = models.ForeignKey('account.Profile', on_delete=models.DO_NOTHING, null = True)
    hashtags = models.ManyToManyField('main.Hashtag', blank = True)
    r_location = models.CharField(max_length=20, null = True, blank = True)
    r_photo = models.ImageField(upload_to='images/', blank = True)
    r_receipt = models.ImageField(upload_to='images/', blank = True)
    r_nickname = models.CharField(max_length=20, null = True, blank = True)
    r_clip = models.ManyToManyField('account.Profile', related_name='r_clip', blank=True)
    r_clips = models.PositiveIntegerField(default=0, verbose_name='조회수')
    r_date = models.DateTimeField('data published')
    r_user = models.ForeignKey('account.Profile', related_name='r_user', on_delete=models.CASCADE, null=True, default='')
    r_like = models.ManyToManyField('account.Profile', related_name='r_likes', blank=True)
    r_likes = models.PositiveIntegerField(default=0, verbose_name='추천수')

    def __str__(self):
        return self.r_title

    @property
    def r_update_counter(self) :
        self.r_clicks += 1 
        self.save() 


class r_comment(models.Model) :
    def __str__(self) :
        return self.text

    r_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='r_comments')
    text = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)
    name = models.ForeignKey('account.Profile', on_delete=models.DO_NOTHING, null = True)
    r_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 
