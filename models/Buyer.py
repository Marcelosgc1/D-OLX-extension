from models.User import User
from models.persistency import Persistency
from models.Seller import Seller

class Buyer(User):
    def __init__(self, name:str, age:int, id:int, phone:int, email:str, password:str):
        self.name=name
        self.age=age
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password
        self.comprados=[]


    def comprar(produto):
        if produto.product_id not in Persistency.get_instance().get_produtos_disponiveis():
            print('Esse produto não está disponivel')
            return False
        print(f"O produto é: {produto.product_name}; {produto.description}")
        confirmacao=input('Tem certeza que esse é o produto que você quer comprar? (S/N): ').upper()
        if confirmacao=='S':
            return True
        
    def realizarComentario(usuario,produto):
        for i in usuario.comprados:
            if i==produto.product_id:
                if produto.comments.get(usuario.id)==None:
                    comentario=input('Realize um comentário sobre esse produto: ')
                    produto.comments[usuario.id]=comentario
                    return True
                return False


#não foi implementado        
    def editarPerfil():
        pass
#não foi implementado
    def permitirNotificacoes():
        pass