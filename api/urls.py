from django.urls import path
from .views import Categoria, RegistrarUsuario, Usuario, UsuarioLogin, Produto

urlpatterns = [
    path('categoria', Categoria.as_view()),
    path('cadastro', RegistrarUsuario.as_view()),
    path('usuario', Usuario.as_view()),
    path('login', UsuarioLogin.as_view()),
    path('produto', Produto.as_view())
]
