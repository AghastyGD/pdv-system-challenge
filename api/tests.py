from django.test import TestCase
from .models import Usuario, Categoria


class UsuarioModelTest(TestCase):
    def test_user_exists(self):
        usuarios = Usuario.objects.count()

        self.assertEqual(usuarios, 0)

    def test_user_email_unique(self):
        usuario = Usuario.objects.create(nome='Augusto', email='augusto@gmail.com', senha='gdpro')
        usuario_2 = Usuario.objects.create(nome ='Joao', email='augusto2@gmail.com', senha='1234')

        self.assertNotEqual(usuario.email, usuario_2.email )

