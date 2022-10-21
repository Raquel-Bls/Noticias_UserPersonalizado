# Obliga a que estes logueado para poder visualizar la vista#
from django.contrib.auth.mixins import LoginRequiredMixin
# Valida los permisos
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comentarios, Noticias
# Para que te regrese a la pagina principal de una manera mas lenta
from django.urls import reverse_lazy


class noticiasPageview(ListView):
    template_name = 'noticias.html'
    model = Noticias
    context_object_name = 'Todas_Noticias'


class noticiasPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'noticias_detalle.html'
    model = Noticias
    context_object_name = 'Todas_Noticias'
    login_url = 'login'


class noticiasPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'noticias_nuevo.html'
    model = Noticias
    fields = ('Titulo', 'Descripcion')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.Autor = self.request.user
        return super().form_valid(form)


class noticiasPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'noticias_editar.html'
    model = Noticias
    fields = ['Titulo', 'Descripcion']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class noticiasPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'noticias_eliminar.html'
    model = Noticias
    fields = "_all_"
    success_url = reverse_lazy('noticias')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class comentriosPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios.html'
    model = Comentarios
    fields = ('comentario',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.noticia_id = self.kwargs['pk']
        return super().form_valid(form)
