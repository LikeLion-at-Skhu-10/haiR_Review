from django.db import models

from free.models import Free 
from QnA.models import Question
from review.models import Review

# Create your models here.

class Hashtag(models.Model) :
    name = models.CharField(max_length=50)
    p_id = models.ForeignKey(Free, on_delete=models.CASCADE, null=True)
    qna_id = models.ForeignKey(Question, on_delete = models.CASCADE, null=True) 
    r_id = models.ForeignKey(Review, on_delete=models.CASCADE, null = True)

    def __str__(self) :
        return self.name  

