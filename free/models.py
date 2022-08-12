from django.db import models

# Create your models here.
class Blog(models.Model):
    p_title = models.CharField(max_length=200)
    p_date = models.DateTimeField('data published')
    p_body = models.TextField()
    p_photo = models.ImageField(upload_to='images/', blank = True)
    p_likes = models.CharField(max_length=20, null = True, blank = True)
    p_clicks = models.PositiveIntegerField(default=0)
    hashtags = models.ManyToManyField('Hashtag', blank = True, null=True, editable=True)

    def __str__(self) :
        return self.p_title

    @property
    def update_counter(self):
        self.p_clicks = self.p_clicks + 1
        self.save()

class p_comment(models.Model) :
    def __str__(self) :
        return self.text

    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=20)

class Hashtag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name