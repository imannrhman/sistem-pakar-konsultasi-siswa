from django.db import models

# Create your models here.
class Behavior(models.Model):
        code = models.CharField(max_length=30)
        name = models.CharField(max_length=250)
        created_at = models.DateTimeField(auto_now_add=True) 
        
        def __str__(self):
                return self.code

class Solution(models.Model):
        behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def code(self):
                return self.behavior.code;

        def problem(self):
                return self.behavior.name;
                


class Problem(models.Model):
        behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        
        def code(self):
                return self.behavior.code;

        def problem(self):
                return self.behavior.name;