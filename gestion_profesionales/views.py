from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from gestion_profesionales.forms import ProfesionaleForm
from .models import Profesionale


class CrearProfesional(CreateView):
    model = Profesionale
    form_class = ProfesionaleForm
    template_name = 'gestion_profesionales/crear_profesionales.html'
    success_url = reverse_lazy('gestion_profesionales:listar_profesional')


class ListadoProfesional(ListView):
    model = Profesionale
    template_name = 'gestion_profesionales/listar_profesionales.html'
    paginate_by = 10
    context_object_name = 'profesionales'
    queryset = Profesionale.objects.all()


class ActualizarProfesional(UpdateView):
    model = Profesionale
    template_name = 'gestion_profesionales/crear_profesionales.html'
    form_class = ProfesionaleForm
    success_url = reverse_lazy('gestion_profesionales:listar_profesional')


class EliminarProfesional(DeleteView):
    model = Profesionale
    success_url = reverse_lazy('gestion_profesionales:listar_profesional')


