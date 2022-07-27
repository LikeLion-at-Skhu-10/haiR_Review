from django.db import models
from distutils.command.upload import upload

# Create your models here.
class QnA(models.Model):    
    q_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length = 200)
    q_date = models.DateTimeField()
    #q_updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to= 'images/' ,blank = True )
    hashtags = models.ManyToManyField('Hashtag' , blank = True)
    def __str__(self):
        return self.title
class QnAComment(models.Model) :
    def __str__(self) :
        return self.text    
    qna_id = models.ForeignKey(QnA, on_delete = models.CASCADE, related_name='comments') 
    text = models.CharField(max_length=50)  

class Hashtag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name             