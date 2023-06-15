from django.forms import ModelForm, widgets
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['comments' , 'likes']

        labels = {
            'title' : 'Title',
            'text' : 'Text',
        }


# title = models.CharField(max_length=20)
#     text = models.TextField(max_length=1000)
#     subject = models.IntegerField(choices=subject_choice, default=1)
#     comments = models.CharField(max_length=100)
#     likes = models.IntegerField(default= 0)