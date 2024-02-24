from models.User import User
class Seller(User):
    def __init__(self, name:str, age:int, id:int, phone, email, user, password):
        super().__init__(name, age, id, phone, email, user, password)
        self.produtos=[]

    def buscarItem():
        pass