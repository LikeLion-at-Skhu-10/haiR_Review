from django.db import models

# Create your models here.

class Question(models.Model):    
    question = models.TextField()
    name = models.ForeignKey('account.User', on_delete=models.DO_NOTHING, null = True)
    q_date = models.DateTimeField('data published')
    q_photo = models.ImageField(upload_to = 'q_images/', blank =True ,null = True)
    hashtags = models.ManyToManyField('main.Hashtag' , blank = True)
    q_clicks = models.PositiveIntegerField(default=0, verbose_name='조회수') 
    q_likes = models.CharField(max_length=20, null = True, blank = True)
    
    def __str__(self):
        return self.question

class Answer(models.Model) :
    def __str__(self) :
        return self.text

    qna_id = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='answers') 
    text = models.TextField(max_length=50)
    create_at = models.DateTimeField(auto_now=True)
    name = models.ForeignKey('account.User', on_delete=models.DO_NOTHING, null = True)
    a_photo = models.ImageField(upload_to = 'a_images/', blank =True ,null = True)
    a_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 
