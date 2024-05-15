from django.urls import path
from news import views

urlpatterns = [
    path('', views.home, name='home'),
    path('random/', views.randomize, name='random'),
    path('calculate/', views.calc, name='calc'),
    path('calculate/<int:number>', views.calc_int, name='calc_int'),
    path('dict/<str:text>', views.get_data, name='det_data'),

]
