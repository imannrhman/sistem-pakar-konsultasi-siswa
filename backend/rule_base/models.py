from django.db import models
from django.db.models.base import Model
from behaviors.models import Behavior
from questions.models import Question
# Create your models here.
class RuleBase(models.Model) :
        behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
        question = models.ManyToManyField(Question)

        def behavior_code(self):
                return self.behavior.code
        
        def questions_code(self):
                return ', '.join((code.code for code in self.question.all()))
