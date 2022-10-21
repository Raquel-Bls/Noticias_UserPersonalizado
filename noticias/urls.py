from django.urls import path
from .views import noticiasPageview, noticiasPageDetail, noticiasPageCreate, noticiasPageUpdate, noticiasPageDelete, comentriosPageCreate

urlpatterns = [
    path('noticias/', noticiasPageview.as_view(), name='noticias'),
    path('noticias/<int:pk>', noticiasPageDetail.as_view(), name='noticias_detalle'),
    path('noticias/nuevo', noticiasPageCreate.as_view(), name='noticias_nuevo'),
    path('noticias/<int:pk>/editar/',
         noticiasPageUpdate.as_view(), name='noticias_editar'),
    path('noticias/<int:pk>/eliminar/',
         noticiasPageDelete.as_view(), name='noticias_eliminar'),
    path('<int:pk>/comentarios/',
         comentriosPageCreate.as_view(), name='comentarios'),

    path('', noticiasPageview.as_view(), name='noticias'),
]
