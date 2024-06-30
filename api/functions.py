from .models import Clientes, Produtos

def get_produto(id): 
    try:
        return Produtos.objects.get(id=id)
        
    except Produtos.DoesNotExist:
        return None

def get_cliente(id):
        try:
           return Clientes.objects.get(id=id)
        
        except Clientes.DoesNotExist:
            return None
