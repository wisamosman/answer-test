from django.db import models
from taggit.managers import TaggableManager



class Answer(models.Model):
    
    name = models.CharField(max_length=100)
    answer = models.TextField(max_length=15000)
    question = models.ForeignKey('Question',related_name='Question_Answer',on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
    


class Question(models.Model):
    question = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    tags = TaggableManager()
    
    
    def __str__(self):
        return self.question



# Create your models here.
