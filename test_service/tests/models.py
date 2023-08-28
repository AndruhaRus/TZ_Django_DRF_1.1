from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    is_correct = models.BooleanField()

class TestResult(models.Model):
    test_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()