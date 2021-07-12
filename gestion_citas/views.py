from datetime import datetime
from time import strptime

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from gestion_citas.forms import Cifaform
from gestion_calendario.forms import CalendarioForm
from .models import Cita
from gestion_calendario.models import Calendario
from gestion_profesionales.models import Profesionale
from django.db.models import Q
from gestion_representantes.models import Representante
from gestion_paciente.models import Paciente


class CrearCita(CreateView):
    model = Cita
    form_class = Cifaform
    template_name = 'gestion_citas/crear_cita.html'
    success_url = reverse_lazy('gestion_citas:listar_cita')


class ActualizarCita(UpdateView):
    model = Cita
    template_name = 'gestion_citas/crear_cita.html'
    form_class = Cifaform
    success_url = reverse_lazy('gestion_citas:listar_cita')


class EliminarCita(DeleteView):
    model = Cita
    success_url = reverse_lazy('gestion_citas:listar_cita')


class ListadoCita(ListView):
    model = Cita
    template_name = 'gestion_citas/listar_cita.html'
    paginate_by = 10
    context_object_name = 'citas'
    queryset = Cita.objects.all()


class Seleccion_especialidad(ListView):
    model = Calendario
    template_name = 'gestion_citas/seleccionar_especialidad.html'
    # context_object_name = 'especialidades'
    queryset = Calendario.objects.values_list('especialidad').distinct()


"""class Disponibilidad(ListView):
    model = Calendario
    template_name = 'gestion_citas/seleccionar_fecha_hora.html'
    context_object_name = 'disponibles'
    queryset = Calendario.objects.filter()


class Disponibilidad2(ListView):
    model = Calendario
    template_name = 'gestion_citas/seleccionar_fecha_hora.html'
    form_class = CalendarioForm

    def get_queryset(self):
        buscar = self.request.GET.get("eleccion", None)
        print(buscar)
        queryset = Calendario.objects.filter(buscar, estado=0)

        return queryset

    def get_context_data(self, **kwargs):
        contexto = {'pacientes': self.get_queryset(), 'form': self.form_class}
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
"""
global var1_1_1
global var2_2_2


def reserva(request):
    global var1_1
    global var2_2
    var1 = 1
    var2 = 1
    var3 = 1
    try:
        if request.GET["especialidad_selec"]:
            var1 = request.GET["especialidad_selec"]
            var1_1 = str(var1)
            lrg = len(var1_1)
            var1_1 = var1_1[2:lrg - 3]
            var1 = var1_1
            qry1 = Calendario.objects.filter(especialidad__icontains=var1_1)
            var1_1_1 = var1_1
            return render(request, "gestion_citas/seleccionar_fecha_hora.html", {'fechas': qry1, 'query': var1_1})

    except:
        if request.GET["fecha"]:
            var2 = request.GET["fecha"]
            print(var1_1)
            print(var2)
            var2_2 = str(var2)
            print(var2_2)
            var2_2_2 = var2_2
            qry2 = Calendario.objects.filter(especialidad__icontains=var1_1, fecha_reserva=var2)
            return render(request, "gestion_citas/seleccionar_hora.html", {'horas': qry2})


def reserva_2(request):
    global var3_3
    form = Cifaform
    if request.GET["hora"]:
        var3 = request.GET["hora"]
        print(var1_1)
        print(var2_2)
        print(var3)
        var3_3 = var3
        print("Hola ")
        # qry3 = Calendario.objects.filter(especialidad__icontains=var1_1, fecha_reserva=var2_2, hora_reserva=var3)
        return render(request, "gestion_citas/confirmar_cita.html",
                      {'especialidad': var1_1, 'fecha': var2_2, 'hora': var3, 'form': form})


def reserva_3(request):
    global var4_4
    global var5_5
    global var6_6
    global var7_7

    if request.POST["rut"]:
        var4 = request.POST["rut"]
        var4_4 = var4
        print(var1_1)
        print(var2_2)
        # correo
        q1 = Representante.objects.values_list('correo').filter(rut__icontains=var4)
        q1_1 = q1[0]
        q1_1 = str(q1_1)
        lrg = len(q1_1)
        q1_1 = q1_1[2:lrg - 3]
        var5_5 = q1_1
        print(q1_1)
        # nombre
        q2 = Representante.objects.values_list('nombres').filter(rut__icontains=var4)
        q2_2 = q2[0]
        q2_2 = str(q2_2)
        lrg = len(q2_2)
        q2_2 = q2_2[2:lrg - 3]
        print(q2)
        # apellidos
        q3 = Representante.objects.values_list('apellidos').filter(rut__icontains=var4)
        q3_3 = q3[0]
        q3_3 = str(q3_3)
        lrg = len(q3_3)
        q3_3 = q3_3[2:lrg - 3]
        print(q3)
        # id representante
        q7 = Representante.objects.values_list('id').filter(rut__icontains=var4)
        print(q7)
        # paciente
        q4 = Paciente.objects.values_list('nombres').filter(representante_id=q7[0])
        q4_4 = q4[0]
        q4_4 = str(q4_4)
        lrg = len(q4_4)
        q4_4 = q4_4[2:lrg - 3]
        var7_7 = q4_4
        print(q4)
        # apellidos
        q5 = Paciente.objects.values_list('apellidos').filter(representante_id=q7[0])
        q5_5 = q5[0]
        q5_5 = str(q5_5)
        lrg = len(q5_5)
        q5_5 = q5_5[2:lrg - 3]
        print(q5)
        # contacto
        q6 = Representante.objects.values_list('contacto').filter(rut__icontains=var4)
        q6_6 = q6[0]
        q6_6 = str(q6_6)
        lrg = len(q6_6)
        q6_6 = q6_6[2:lrg - 3]
        var6_6 = q6_6

        print(q6)
        # mostrar esos datos y despues guardar los datos con un botón de confirmación
        return render(request, "gestion_citas/guardar_cita.html",
                      {'nombres_a': q2_2, 'apellidos_a': q3_3, 'correo_a': q1_1, 'contacto_a': q6_6, 'nombres_p': q4_4,
                       'apellidos_p': q5_5, 'especialidad': var1_1, 'fecha': var2_2, 'hora': var3_3})

        # utilizar el método save() para guardar los datos en la tabla de citas


def guardar_reserva(request):
    save_res = Cita(representante=var4_4, correo=var5_5, contacto=var6_6, paciente=var7_7, especialista="",
                    especialidad=var1_1, hora_atencion=var3_3, fecha_atencion=var2_2)
    save_res.save()
    return render(request, "gestion_citas/gracias_reserva.html")
