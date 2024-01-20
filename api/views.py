from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Categoria, Produtos
from .serializers import UsuarioSerializer, CategoriaSerializer, ProdutosSerializer, ClientesSerializer


# FUNÇÃO PARA PEGAR PEGAR ID DE PRODUTO
def get_object(id):
    try:
        return Produtos.objects.get(id=id)
        
    except Produtos.DoesNotExist:
        return None
  
# ========================================= ENDPOINTS =================================================    

# CATEGORIA
class CategoriaView(APIView):

    def get(self, request, *args, **kwargs):   # Listar as categorias
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# USUARIO
class UsuarioView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):   # Detalhes do perfil do usuario
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):    # Atualizer perfil
        serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)

# CADASTAR UM NOVO USER
class RegistrarUsuarioView(APIView):
    def post(self, request, *args, **kwargs):  # Cadastrar um novo usuario
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

# PRODUTO
class ProdutoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):  # Cadastrar um novo produto
        serializer = ProdutosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.to_representation(instance=serializer.instance), status=status.HTTP_201_CREATED)
    
    def put(self, request, id, *args, **kwargs):  # Atualizer um produto
       produto = get_object(id)
       serializer = ProdutosSerializer(produto, data = request.data, partial = True)
       serializer.is_valid(raise_exception = True)
       serializer.save()
      
       return Response(serializer.data)
   
    def get(self, request, *args, **kwargs):    # Listar produtos e filtrar por categoria
        categoria_id = request.query_params.get('categoria_id')
        if categoria_id:
            produtos = Produtos.objects.filter(categoria_id=categoria_id)
            
        else: 
            produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id, *args, **kwargs):   # Remover um produto fornecendo o ID
        produto = get_object(id)
        produto.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
# DETALHE DE UM PRODUTO    
class ProdutoDetailView(APIView):
    def get(self, request, id, *args, **kwargs):  # Mostrar detalhes de um produto
        produtos_instance = get_object(id)
        if not produtos_instance:
            return Response(
                {"res": "Produto nao encontrado"},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializer = ProdutosSerializer(produtos_instance)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# CLIENTE
class ClienteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs): # Cadastrar um novo cliente
        serializer = ClientesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.to_representation(instance=serializer.instance), status=status.HTTP_201_CREATED)

