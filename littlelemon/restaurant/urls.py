#define URL route for index() view
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
