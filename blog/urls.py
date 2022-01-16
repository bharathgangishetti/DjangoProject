from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('blog/', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]