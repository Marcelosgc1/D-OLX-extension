from models.User import User
class Buyer(User):
    def __init__(self, name:str, age:int, id:int):
        super().__init__(name, age, id)
