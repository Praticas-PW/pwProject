from django.shortcuts import render, redirect
from . models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'index.html')


def about_me(request):
    return render(request, 'about_me.html')


def licenciatura(request):
    return render(request, 'licenciatura.html')

def projetos(request):
    return render(request, 'projetos.html')

def editPost(request):
    return render(request, 'editPost.html')

def sing_in(request):
    return render(request, 'sing_in.html')


def blog(request):

    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {'posts': Post.objects.all(), 'form': form}
    return render(request, 'blog.html', context)





@login_required
def deletePost(request, post_id):
    Post.objects.get(pk = post_id).delete()
    return HttpResponseRedirect(reverse('blog'))



def web(request):
    return render(request, 'web.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                           username=username,
                           password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')