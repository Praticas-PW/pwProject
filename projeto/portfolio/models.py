from django.db import models

# Create your models here.
class Post(models.Model):

    subject_choice = [(1,'Geral'), (2,'Tecnologias'), (3,'Cultura'), (4, 'Edcucacao')]

    title = models.CharField(max_length=20)
    text = models.TextField(max_length=1000)
    subject = models.IntegerField(choices=subject_choice, default=1)
    comments = models.CharField(max_length=100)
    likes = models.IntegerField(default= 0)

    def __str__(self):
        return self.title[:20]
    



class User(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name[:20]
    
