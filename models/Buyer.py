from models.User import User
from persistency import Persistency

class Buyer(User):
    def __init__(self, name:str, age:int, id:int, phone:int, email:str, password:str):
        self.name=name
        self.age=age
        if id in Persistency.get_instace().get_usuarios():
            return False
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password        
        self.produtos=[]

    def buscarProduto():
        pass

    def comprar():
        pass

    def editarPerfil():
        pass