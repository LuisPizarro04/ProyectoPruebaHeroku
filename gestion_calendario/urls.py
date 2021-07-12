from django.urls import path
from .views import CrearCalendario, ListadoCalendario, ActualizarCalendario, EliminarCalendario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_reserva/', login_required(CrearCalendario.as_view()), name='crear_reserva'),
    path('listar_reserva/', login_required(ListadoCalendario.as_view()), name='listar_reserva'),
    path('editar_reserva/<int:pk>', login_required(ActualizarCalendario.as_view()), name='editar_reserva'),
    path('eliminar_reserva/<int:pk>', login_required(EliminarCalendario.as_view()), name='eliminar_reserva'),
]
