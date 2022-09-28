#URLS de la APP para coordinar con el URSL.py del proyecto.
#Informo con formato path('nombre de clase/', clase)

from django.urls import path
from .views import *


urlpatterns = [
      
    path('crearmensaje/', crearmensaje, name='crearmensaje'),
    path('mensajes/', mis_mensajes, name='mensajes'),

    ]

