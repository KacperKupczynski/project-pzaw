from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # 50 first chars

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    wpm = models.FloatField()  # APM (actions per minute)
    accuracy = models.FloatField()  # Accuracy of the typing
    created_at = models.DateTimeField(auto_now_add=True)  # Date of result creation

    def __str__(self):
        return f"WPM: {self.wpm} - Accuracy: {self.accuracy}%"