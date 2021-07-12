from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from gestion_calendario.forms import CalendarioForm
from .models import Calendario


class CrearCalendario(CreateView):
    model = Calendario
    form_class = CalendarioForm
    template_name = 'gestion_calendario/crear_calendario.html'
    success_url = reverse_lazy('gestion_calendario:listar_reserva')


class ListadoCalendario(ListView):
    model = Calendario
    template_name = 'gestion_calendario/listar_calendario.html'
    paginate_by = 10
    context_object_name = 'calendarios'
    queryset = Calendario.objects.all()


class ActualizarCalendario(UpdateView):
    model = Calendario
    template_name = 'gestion_calendario/crear_calendario.html'
    form_class = CalendarioForm
    success_url = reverse_lazy('gestion_calendario:listar_reserva')


class EliminarCalendario(DeleteView):
    model = Calendario
    success_url = reverse_lazy('gestion_calendario:listar_reserva')
