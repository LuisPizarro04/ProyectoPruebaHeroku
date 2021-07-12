from django.urls import path
from . import views
from .views import CrearCita, ListadoCita, ActualizarCita, EliminarCita, Seleccion_especialidad
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_cita/', login_required(CrearCita.as_view()), name='crear_cita'),
    path('listar_cita/', login_required(ListadoCita.as_view()), name='listar_cita'),
    path('seleccionar_especialidad/', login_required(Seleccion_especialidad.as_view()),
         name='seleccionar_especialidad'),
    path('editar_cita/<int:pk>', login_required(ActualizarCita.as_view()), name='editar_cita'),
    path('eliminar_cita/<int:pk>', login_required(EliminarCita.as_view()), name='eliminar_cita'),
    path('reserva/', views.reserva, name='selec_espe'),
    path('seleccionar_fecha/', login_required(views.reserva), name='selec_fecha'),
    path('reserva_final/', login_required(views.reserva_2), name='reserva_final'),
    path('reserva_final_2/', login_required(views.reserva_3), name='reserva_final_2'),
    path('guardar_reserva/', login_required(views.guardar_reserva), name='guardar_reserva'),

]
