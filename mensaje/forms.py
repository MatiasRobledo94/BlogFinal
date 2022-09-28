from datetime import datetime
from email.policy import default
from secrets import choice
from urllib import request
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import *
from .models import *

class CrearMensaje(forms.Form):
    receptor= forms.CharField(max_length=50)
    mensaje=RichTextFormField()