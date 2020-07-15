from django.urls import path
from vistaprevia import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('cargar/', views.cargar_imagen, name='cargar'),
    path('<int:producto_id>/ver/', views.ver_imagen, name='ver'),
    path('verimagenes', views.ver_imagenes, name='verimagenes'),
]
