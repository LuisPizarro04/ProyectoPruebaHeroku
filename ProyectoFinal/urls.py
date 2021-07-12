"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from usuario.views import logoutUsuario, Login, Inicio
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(('usuario.urls', "usuario"))),
    path('gestion_calendario/', include(('gestion_paciente.urls', "gestion_paciente"))),
    path('gestion_paciente/', include(('gestion_calendario.urls', "gestion_calendario"))),
    path('gestion_profesionales/', include(('gestion_profesionales.urls', "gestion_profesionales"))),
    path('gestion_representantes/', include(('gestion_representantes.urls', "gestion_representantes"))),
    path('gestion_citas/', include(('gestion_citas.urls', "gestion_citas"))),
    path('', login_required(Inicio.as_view()), name='index'),
    path('accounts/login/', Login.as_view(template_name="login.html"), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('reset/password_reset', PasswordResetView.as_view(template_name="password/password_reset_form.html", email_template_name="password/password_reset_email.html"),
         name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name="password/password_reset_done.html"),
         name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm"
                                                                                    ".html"),
         name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"),
         name='password_reset_complete'),
]