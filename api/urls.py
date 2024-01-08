from django.urls import path
from .views import CategoriaApiView, RegistrarUsuario, UsuarioApiView, UsuarioLogin

urlpatterns = [
    path('categoria', CategoriaApiView.as_view()),
    path('cadastro', RegistrarUsuario.as_view()),
    path('usuario', UsuarioApiView.as_view()),
    path('login', UsuarioLogin.as_view()),
]
