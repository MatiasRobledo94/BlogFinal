from django.contrib import admin
from django.contrib import admin
from mensaje.models import *

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'mensaje', 'autor', 'receptor' )

admin.site.register(Mensaje, MensajeAdmin)
