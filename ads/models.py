from django.db import models

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)