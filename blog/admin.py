from django.contrib import admin
from blog.models import *

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha', 'autor', 'categoria' )

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'imagen', 'bio', 'link')

admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Avatar)
admin.site.register(Perfil, PerfilAdmin)
