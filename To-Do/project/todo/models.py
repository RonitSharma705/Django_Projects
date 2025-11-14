from django.db import models

class Todo(models.Model):
    Title=models.CharField(max_length=50)
    Description=models.TextField(max_length=100)
    Complete=models.BooleanField(default=False)
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
