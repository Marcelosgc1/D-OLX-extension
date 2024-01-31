from User import User
class Buyer(User):
    def __init__(self, name, age, cpf):
        super().__init__(name, age, cpf)
        self.produtos=[]
        