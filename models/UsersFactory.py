from persistency import Persistency
from Buyer import Buyer
from Seller import Seller

class User_Factory:
    @staticmethod
    def criar_Usuario(name, age, id, phone, email, password, tipo):
        if id in Persistency.get_instance().get_usuarios():
            print('sextouuuu')
            return False
        elif tipo=='Buyer':
            return Buyer(name, age, id, phone, email, password)
        elif tipo=='Seller':
            return Seller(name, age, id, phone, email, password)
        else:
            return None