from ast import JoinedStr
import http
from inspect import formatargvalues
from modulefinder import replacePackageMap
from nturl2path import url2pathname
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import date
import datetime
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import *
from blog.forms import *
from blog.views import *

@login_required
def crearmensaje(request):
    receptor=request.user
    if request.method == "POST":
        mensaje = CrearMensaje(request.POST)
        if mensaje.is_valid():
            informacion = mensaje.cleaned_data
            mensaje = Mensaje(mensaje=informacion['mensaje'], fecha=datetime.today(), autor=request.user, receptor=informacion['receptor'])
            mensaje.save()
            return render(request, "blog/inicio.html", {"mensaje":f"El mensaje se ha enviado correctamente."})
    else:
        mensaje = CrearMensaje()
        return render (request, "blog/crearmensaje.html", {'mensajes': mensaje,'imagen':obtenerAvatar(request)})

@login_required 
def mis_mensajes(request):
    receptor=request.user
    mensaje=Mensaje.objects.filter(receptor=receptor) 
    if (len(mensaje)!=0):
        return render (request, 'blog/mensajes.html', {'mensajes': mensaje,'imagen':obtenerAvatar(request)})
    else:
        return render(request, "blog/mensajes.html", {'imagen':obtenerAvatar(request)})