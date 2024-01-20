from django.urls import path
from .views import (CategoriaView, RegistrarUsuarioView, 
                    UsuarioView, UsuarioLoginView, ProdutoView, 
                    ClienteView, ProdutoDetailView)

urlpatterns = [
    path('categoria', CategoriaView.as_view()),
    path('cadastro', RegistrarUsuarioView.as_view()),
    path('usuario', UsuarioView.as_view()),
    path('login', UsuarioLoginView.as_view()),
    path('produto', ProdutoView.as_view(), name='produto-list'),
    path('produto/<int:id>', ProdutoView.as_view(), name='produto-update-delete'),
    path('produto-detail/<int:id>', ProdutoDetailView.as_view(), name='produto-detail'),
    path('cliente', ClienteView.as_view(), name='client-list-add')
]
