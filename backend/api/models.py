from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # 50 first chars
    

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    wpm = models.FloatField()  
    accuracy = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.wpm} WPM"
    
