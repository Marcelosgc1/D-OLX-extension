from models.User import User
from persistency import Persistency

class Seller(User):
    def __init__(self, name:str, age:int, id:int, phone, email, password):
        self.name=name
        self.age=age
        if id in Persistency.get_instace().get_usuarios():
            return False
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password        
        self.produtos=[]

    def publicarProduto():
        pass

    def vender():
        pass

    def editarPerfil():
        pass