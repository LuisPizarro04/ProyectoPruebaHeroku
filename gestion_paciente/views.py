from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from gestion_paciente.forms import PacienteForm, FichaForm
from .models import Paciente, Ficha


class CrearPaciente(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'gestion_paciente/crear_paciente.html'
    success_url = reverse_lazy('gestion_paciente:listar_paciente')


class ListadoPaciente(ListView):
    model = Paciente
    template_name = 'gestion_paciente/listar_paciente.html'
    context_object_name = 'pacientes'
    queryset = Paciente.objects.all()


class ActualizarPaciente(UpdateView):
    model = Paciente
    template_name = 'gestion_paciente/crear_paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('gestion_paciente:listar_paciente')


class EliminarPaciente(DeleteView):
    model = Paciente
    success_url = reverse_lazy('gestion_paciente:listar_paciente')


class CrearFicha(CreateView):
    model = Ficha
    form_class = FichaForm
    template_name = 'gestion_paciente/crear_ficha.html'
    success_url = reverse_lazy('gestion_paciente:listar_ficha')


class ListadoFicha(ListView):
    model = Ficha
    template_name = 'gestion_paciente/listar_ficha.html'
    context_object_name = 'fichas'
    queryset = Ficha.objects.all()


class ActualizarFicha(UpdateView):
    model = Ficha
    template_name = 'gestion_paciente/crear_ficha.html'
    form_class = FichaForm
    success_url = reverse_lazy('gestion_paciente:listar_ficha')


class EliminarFicha(DeleteView):
    model = Ficha
    success_url = reverse_lazy('gestion_paciente:listar_ficha')

