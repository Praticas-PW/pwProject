
from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.home, name='home'),
    path('about_me', views.about_me, name="about_me"),
    path('licenciatura', views.licenciatura, name='licenciatura'),
    path('projetos', views.projetos, name='projetos')

]
