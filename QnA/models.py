from django.db import models

# Create your models here.

class Question(models.Model):    
    question = models.TextField()
    
    q_date = models.DateTimeField('data published')
    q_photo = models.ImageField(upload_to = 'q_images/', blank =True ,null = True)
    hashtags = models.ManyToManyField('main.Hashtag' , blank = True)
   
    q_clicks = models.PositiveIntegerField(default=0, verbose_name='조회수') 
   

    q_likes = models.PositiveIntegerField(default=0, verbose_name='추천수')
    
    def __str__(self):
        return self.question

    def q_summary(self) : 
        return self.question[:20]

    @property
    def q_update_counter(self) :
        self.q_clicks += 1 
        self.save() 

class Answer(models.Model) :
    def __str__(self) :
        return self.text

    qna_id = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='answers') 
    text = models.TextField(max_length=50)
    create_at = models.DateTimeField(auto_now=True)
   
    a_photo = models.ImageField(upload_to = 'a_images/', blank =True ,null = True)
    a_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 
