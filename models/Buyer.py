from models.User import User
class Buyer(User):
    def __init__(self, name:str, age:int, id:int, phone, email, password):
        super().__init__(name, age, id, phone, email, password)

    def publicarProduto():
        pass