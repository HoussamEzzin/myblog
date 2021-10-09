from django.urls import path
from . import views


#this is where the urls is :
urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about")
]
