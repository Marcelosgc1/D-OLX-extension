from models.User import User
class Seller(User):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.produtos=[]
