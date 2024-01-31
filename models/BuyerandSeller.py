from models.Buyer import Buyer
from models.Seller import Seller
class Buyer_and_Seller(Buyer,Seller):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
    

    def testeee(self):
        print('alo?')