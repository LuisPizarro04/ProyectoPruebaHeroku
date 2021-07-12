from django.urls import path
from .views import CrearPaciente, ListadoPaciente, ActualizarPaciente, EliminarPaciente, CrearFicha, ListadoFicha, ActualizarFicha, EliminarFicha
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_paciente/', login_required(CrearPaciente.as_view()), name='crear_paciente'),
    path('listar_paciente/', login_required(ListadoPaciente.as_view()), name='listar_paciente'),
    path('editar_paciente/<int:pk>', login_required(ActualizarPaciente.as_view()), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>', login_required(EliminarPaciente.as_view()), name='eliminar_paciente'),
    path('crear_ficha/', login_required(CrearFicha.as_view()), name='crear_ficha'),
    path('listar_ficha/', login_required(ListadoFicha.as_view()), name='listar_ficha'),
    path('editar_ficha/<int:pk>', login_required(ActualizarFicha.as_view()), name='editar_ficha'),
    path('eliminar_ficha/<int:pk>', login_required(EliminarFicha.as_view()), name='eliminar_ficha'),

]
