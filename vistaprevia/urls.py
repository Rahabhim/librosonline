from django.urls import path
from vistaprevia import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('cargar/', views.cargar_imagen, name='cargar'),
]
