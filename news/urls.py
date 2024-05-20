from django.urls import path
from news import views

urlpatterns = [
    path('home/', views.home, name='home')
]
