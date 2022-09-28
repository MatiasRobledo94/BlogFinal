from email import contentmanager
from urllib import request
from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import *   

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Mensaje(models.Model):
    fecha=models.DateField(auto_now_add=True)
    mensaje=RichTextField(blank=True, null=True)
    autor=models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    receptor=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Mensajes"