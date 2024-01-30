from django.urls import path
from .views import (CategoriaView, ClienteDetailView, RegistrarUsuarioView, UsuarioView, 
                    UsuarioLoginView, ProdutoView, ClienteView, ProdutoDetailView, PedidoView, ClientePedidosView)

urlpatterns = [
    path('categoria', CategoriaView.as_view()),
    path('cadastro', RegistrarUsuarioView.as_view()),
    path('usuario', UsuarioView.as_view()),
    path('login', UsuarioLoginView.as_view()),
    path('produto', ProdutoView.as_view(), name='adicionar-e-listar-produtos'),
    path('produto/<int:id>', ProdutoView.as_view(), name='produto-atualizar-remover'),
    path('produto-detail/<int:id>', ProdutoDetailView.as_view(), name='detalhe-do-produto'),
    path('cliente', ClienteView.as_view(), name='adicionar-e-listar-clientes'),
    path('cliente/<int:id>', ClienteView.as_view(), name='atualizar-cliente'),
    path('cliente-detail/<int:id>', ClienteDetailView.as_view(), name='detalhe-do-cliente'),
    path('pedido', PedidoView.as_view(), name='registrar_pedido'),
    path('pedidos/<int:cliente_id>/', ClientePedidosView.as_view(), name='listar-pedidos-de-um-cliente')
    
]
