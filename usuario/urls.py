from django.urls import path
from usuario.views import ListadoUsuario, RegistrarUsuario, EliminarUsuario, ActualizarUsuario, Perfil, NewUser
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar_usuario/', ListadoUsuario.as_view(), name='listar_usuario'),
    path('registrar_usuario/', RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('editar_usuario/<int:pk>', ActualizarUsuario.as_view(), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>', EliminarUsuario.as_view(), name='eliminar_usuario'),
    path('perfil/<int:pk>', Perfil.as_view(), name='perfil'),
    path('newuser/', NewUser.as_view(), name='newuser'),

]