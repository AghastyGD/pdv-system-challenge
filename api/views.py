from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .functions import get_cliente, get_produto
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Categoria, Produtos, Clientes, Pedidos
from .serializers import (UsuarioSerializer, CategoriaSerializer, 
ProdutosSerializer, ClientesSerializer, PedidosSerializer, PedidosProdutosSerializer)


class CategoriaView(APIView):

    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UsuarioView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):  
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):  
        serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)

class RegistrarUsuarioView(APIView):
    def post(self, request, *args, **kwargs): 
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.to_representation(instance=serializer.instance), status=status.HTTP_201_CREATED)

class UsuarioLoginView(APIView):
    def post (self, request, *args, **kwargs):
        email = request.data.get('email')
        senha = request.data.get('senha')

        user = authenticate(request, email=email, password=senha)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'As credenciais estão inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class ProdutoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = ProdutosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.to_representation(instance=serializer.instance), status=status.HTTP_201_CREATED)
    
    def put(self, request, id, *args, **kwargs):
       produto = get_produto(id)
       serializer = ProdutosSerializer(produto, data = request.data, partial = True)
       serializer.is_valid(raise_exception = True)
       serializer.save()
      
       return Response(serializer.data, status=status.HTTP_200_OK)
   
    def get(self, request, *args, **kwargs):
        categoria_id = request.query_params.get('categoria_id')
        if categoria_id:
            produtos = Produtos.objects.filter(categoria_id=categoria_id)
            
        else: 
            produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id, *args, **kwargs): 
        produto = get_produto(id)
        produto.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
   
class ProdutoDetailView(APIView):
    def get(self, request, id, *args, **kwargs): 
        produtos_instance = get_produto(id)
        if not produtos_instance:
            return Response(
                {"res": "Produto nao encontrado"},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializer = ProdutosSerializer(produtos_instance)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClienteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs): 
        serializer = ClientesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.to_representation(instance=serializer.instance), 
                        status=status.HTTP_201_CREATED)
        
    def put(self, request, id, *args, **kwargs):
        cliente = get_cliente(id)
        serializer = ClientesSerializer(cliente, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data)
    
    def get(self, request, *args, **kwargs): 
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
      
class ClienteDetailView(APIView):
    def get(self, request, id, *args, **kwargs): 
        cliente_instance = get_cliente(id)
        if not cliente_instance:
            return Response(
                {"res": "Cliente nao encontrado"},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializer = ClientesSerializer(cliente_instance)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PedidoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = PedidosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
      pedidos = Pedidos.objects.all()
      serializer = PedidosSerializer(pedidos, many=True)
      
      return Response(serializer.data, status=status.HTTP_200_OK)

class ClientePedidosView(APIView):
  def get(self, request, cliente_id, *args, **kwargs):
    cliente = get_object_or_404(Clientes, id=cliente_id)
    cliente_pedidos = Pedidos.objects.filter(cliente_id=cliente_id)
    
    serializer = PedidosSerializer(cliente_pedidos, many=True)
      
    return Response(serializer.data, status=status.HTTP_200_OK)