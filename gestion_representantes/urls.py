from django.urls import path
from .views import CrearRepresentante, ListadoRepresentante, ActualizarRepresentante, EliminarRepresentante
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_representante/', login_required(CrearRepresentante.as_view()), name='crear_representante'),
    path('listar_representante/', login_required(ListadoRepresentante.as_view()), name='listar_representante'),
    path('editar_representante/<int:pk>', login_required(ActualizarRepresentante.as_view()), name='editar_representante'),
    path('eliminar_representante/<int:pk>', login_required(EliminarRepresentante.as_view()), name='eliminar_representante'),

]
