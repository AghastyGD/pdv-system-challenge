from rest_framework import serializers
from .models import Usuario, Categoria, Produtos, Clientes, Pedidos, PedidosProdutos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
     
class PedidosProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosProdutos
        fields = '__all__'
        
        
class PedidosSerializer(serializers.ModelSerializer):
    pedido_produtos = PedidosProdutosSerializer(many=True, read_only=True)
    class Meta:
        model = Pedidos
        fields = '__all__'
        
   
    