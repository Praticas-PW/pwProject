
from django.urls import path, include
from . import views


urlpatterns = [
    path('' , views.home, name='home'),
    path('about_me', views.about_me, name="about_me"),
    path('licenciatura', views.licenciatura, name='licenciatura'),
    path('projetos', views.projetos, name='projetos'),
    path('blog', views.blog, name ='blog'),
    path('web', views.web, name='web'),
    path('blog/deletePost/ <int:post_id>', views.deletePost,name='deletePost'),
    path('login', views.login_view, name = 'login'),
    path('sing_in', views.sing_in, name = 'sing_in'),
    path('create_user', views.create_user_view, name='create_user'),
    path('logout', views.logout_view, name='logout'),
    path('blog/likePost/<int:post_id>', views.likePost, name ='likePost'),
    
]
