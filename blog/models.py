from django.db import models

# Create your models here.

class BlogContent(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
