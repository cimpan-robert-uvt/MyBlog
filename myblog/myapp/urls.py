from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('home/', views.home, name='home'),
path('form/', views.form, name='form'),
path('gallery/', views.gallery, name='gallery'),
]