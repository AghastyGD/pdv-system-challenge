from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
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
    def post (self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.to_representation(instance=serializer.instance), status=status.HTTP_201_CREATED)


class UsuarioList(APIView):
    def get (self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        serialier = UsuarioSerializer(usuarios, many=True)

        return Response(serialier.data, status=status.HTTP_200_OK)

#class UserAuth(BaseAuthentication):
 #   def post (self, request, *args, **kwargs):
  #      user_name = Usuario(request.POST, instance=request.nome)

class UsuarioLogin(APIView):
    def post (self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        usuario = Usuario.objects.get(id)

        if serializer.data(id) == usuario(id):
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.to_representation(instance=serializer.instance), status=status.HTTP_202_ACCEPTED)

        else:
            print("As informacoes estao incorretas, favor tente de novo")


class UserAuth(APIView):
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [IsAuthenticated]
   

    def get(self, request, format=None):
        self.user_name = Usuario.objects.all()
        content = {
            'user': str(request.user)
        }
    
        return Response(content)
