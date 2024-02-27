from models.User import User
from models.Product import Product
from persistency import Persistency

class Seller(User):
    def __init__(self, name:str, age:int, id:int, phone:int, email:str, password:str):
        self.name=name
        self.age=age
        if id in Persistency.get_instace().get_usuarios():
            return False
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password        
        self.produtos=[]

    def criarEPublicarProduto(product_name,description,fabrication_date,genre,location,new_product,quantity,seller_id,seller_name,dic_produtos_disponiveis):
        novoProduto=Product(product_name,description,fabrication_date,seller_id,seller_name,genre,location,new_product,len(dic_produtos_disponiveis)+1,quantity)
        dic_produtos_disponiveis[novoProduto.product_id]=novoProduto

    def vender():
        pass

    def editarPerfil():
        pass