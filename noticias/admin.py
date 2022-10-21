from django.contrib import admin
from .models import Comentarios, Noticias
# Register your models here.


# class ComentarioInline(admin.StackedInline):
#   model = Comentarios

class ComentarioInline(admin.TabularInline):
    model = Comentarios


class NoticiasAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInline
    ]


admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Comentarios)
