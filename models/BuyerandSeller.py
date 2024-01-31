from Buyer import Buyer
from Seller import Seller
class Buyer_and_Seller(Buyer,Seller):
    def __init__(self, name, age, cpf):
        super().__init__(name, age, cpf)