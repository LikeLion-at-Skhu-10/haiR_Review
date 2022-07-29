from django.db import models

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
    r_clicks = models.PositiveIntegerField(default=1, verbose_name='조회수')
    r_date = models.DateTimeField('data published')
    r_likes = models.CharField(max_length=20, null = True, blank = True)

    def __str__(self):
        return self.r_title

class r_comment(models.Model) :
    def __str__(self) :
        return self.text

    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=20)

class Hashtag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name