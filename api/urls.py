from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello-world/', views.hello_world, name='hello_world'),
]