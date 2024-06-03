from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.detail, name='detail'),
]
