from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Categoria, Usuario
from .serializers import UsuarioSerializer, CategoriaSerializer


class CategoriaApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Listar as categorias
        '''
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UsuarioApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class RegistrarUsuario(APIView):
    def post(self, request, *args, **kwargs):
        self.permission_classes = [AllowAny]
        if request.user.is_authenticated:
            return Response({'detail': 'Você já esta logado.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.to_representation(instance=serializer.instance), status=status.HTTP_201_CREATED)

class UsuarioLogin(APIView):
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
       

