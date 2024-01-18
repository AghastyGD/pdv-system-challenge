from django.urls import path
from .views import CategoriaView, RegistrarUsuarioView, UsuarioView, UsuarioLoginView, ProdutoView

urlpatterns = [
    path('categoria', CategoriaView.as_view()),
    path('cadastro', RegistrarUsuarioView.as_view()),
    path('usuario', UsuarioView.as_view()),
    path('login', UsuarioLoginView.as_view()),
    path('produto', ProdutoView.as_view())
]
