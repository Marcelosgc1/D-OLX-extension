from User import User
class Seller(User):
    def __init__(self, name, age, cpf):
        super().__init__(name, age, cpf)
        