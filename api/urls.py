from django.urls import path
from .views import CategoriaApiView, UsuarioApiView, UsuarioList, UsuarioLogin

urlpatterns = [
    path('categoria', CategoriaApiView.as_view()),
    path('usuario', UsuarioApiView.as_view()),
    path('user-list', UsuarioList.as_view()),
    path('login', UsuarioLogin.as_view()),

]
