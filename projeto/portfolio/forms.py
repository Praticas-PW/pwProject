from django.forms import ModelForm, widgets
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['comments']