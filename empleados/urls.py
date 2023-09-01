from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('procesar-formulario/', views.process_form, name='process_form'),
]
