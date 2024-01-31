from models.User import User
class Seller(User):
    def __init__(self, name:str, age:int, id:int):
        super().__init__(name, age, id)
        self.produtos=[]
