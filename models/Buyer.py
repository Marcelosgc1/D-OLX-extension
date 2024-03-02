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


    def comprar(self, produto, quantidade_para_comprar):
        if produto.quantity==0:
            print('Esse produto não está disponivel no momento')
            return False
        elif produto.quantity<quantidade_para_comprar:
            print(f"Esse produto tem apenas {produto.quantity} exemplares.")
            return False
        print(f"O produto é: {produto.product_name}; {produto.description}, por {produto.preco} a uniadde")
        confirmacao=input('Tem certeza que esse é o produto que você quer comprar? (S/N): ').upper()
        if confirmacao=='S':
            return True
        
    def realizarComentario(self,produto):
        comprado=0
        for i in self.comprados:
            if i==produto.product_id:
                comprado=1
                if produto.comments.get(self.id)==None:
                    comentario=input('Realize um comentário sobre esse produto: ')
                    produto.comments[self.id]=comentario
                    return True
                return False
            if comprado==0:
                print('Você não pode comentar sobre o produto sem ter comprado.')
                return False


#não foi implementado        
    def editarPerfil():
        pass
#não foi implementado
    def permitirNotificacoes():
        pass