from django.db import models

# Create your models here.
class Question(models.Model) :
        code = models.CharField(max_length=30)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True) 

        def __str__(self):
                return self.code

class Answer(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        value = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
