from abc import ABC, abstractclassmethod
from models.persistency import Persistency

class User(ABC):
    @abstractclassmethod
    def __init__(self, name:str, age:int, id:int, phone:int, email:str, password:str):
        self.name=name
        self.age=age
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password

    @abstractclassmethod
    def editarPerfil():
        pass