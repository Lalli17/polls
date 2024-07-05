from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option
    
class Feedback(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100, blank=True, null=True)
    option_4 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question