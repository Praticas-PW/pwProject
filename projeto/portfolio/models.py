from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    comments = models.CharField(max_length=100)


    def __str__(self):
        return self.title
        