from django.db import models

# Create your models here.

class Notes(models.Model):
    Title = models.CharField(max_length=100)
    Note = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
    