from abc import ABC, abstractclassmethod
from persistency import Persistency

class User(ABC):
    @abstractclassmethod
    def __init__(self, name:str, age:int, id:int, phone, email, password):
        self.name=name
        self.age=age
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password

    @abstractclassmethod
    def editarPerfil():
        pass