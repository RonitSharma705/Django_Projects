from django.db import models

class Books(models.Model):
    Title=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Publish_date=models.DateField()
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title