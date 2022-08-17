from tkinter import CASCADE
from django.db import models

# Create your models here.

#자유게시판 
class Free(models.Model):
    p_title = models.CharField(max_length=200)
    name = models.ForeignKey('account.User', on_delete=models.CASCADE, null = True)
    p_date = models.DateTimeField('data published')
    p_body = models.TextField()
    p_photo = models.ImageField(upload_to='images/', blank = True)
    p_likes = models.CharField(max_length=20, null = True, blank = True)
    p_clicks = models.PositiveIntegerField(default=1, verbose_name='조회수')
    hashtags = models.ManyToManyField('main.Hashtag', blank = True, null=True, editable=True)

    def __str__(self) : 
        return self.p_title

#댓글
class p_comment(models.Model) :
    def __str__(self) :
        return self.text

    p_id = models.ForeignKey(Free, on_delete=models.CASCADE, null=True, related_name='p_comments')
    text = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)
    name = models.ForeignKey('account.User', on_delete=models.DO_NOTHING, null = True)
    p_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 