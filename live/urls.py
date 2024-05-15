from django.urls import path
from live import views

urlpatterns = [
    path('', views.home, name='home'),

]