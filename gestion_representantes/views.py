from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from gestion_representantes.forms import RepresentanteForm
from .models import Representante


class CrearRepresentante(CreateView):
    model = Representante
    form_class = RepresentanteForm
    template_name = 'gestion_representantes/crear_representantes.html'
    success_url = reverse_lazy('gestion_representantes:listar_representante')


class ListadoRepresentante(ListView):
    model = Representante
    template_name = 'gestion_representantes/listar_representantes.html'
    paginate_by = 10
    context_object_name = 'representantes'
    queryset = Representante.objects.all()


class ActualizarRepresentante(UpdateView):
    model = Representante
    template_name = 'gestion_representantes/crear_representantes.html'
    form_class = RepresentanteForm
    success_url = reverse_lazy('gestion_representantes:listar_representante')


class EliminarRepresentante(DeleteView):
    model = Representante
    success_url = reverse_lazy('gestion_representantes:listar_representante')
