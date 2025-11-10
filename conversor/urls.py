from django.urls import path
from . import views

urlpatterns = [
    path('', views.convertir_binario, name='index'),
]