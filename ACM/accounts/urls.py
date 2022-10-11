from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  #aquí se mandan llamar a las vistas junto con su direccion exacta
    path('register/', views.register, name='register'),
    path('logout/', views.login, name='logout'),
    path('home/', views.home, name="home"),
]