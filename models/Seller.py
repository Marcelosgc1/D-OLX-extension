from models.User import User
from models.Product import Product
from models.persistency import Persistency

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
        
    def criarEPublicarProduto(product_name,description,fabrication_date,genre,location,new_product,quantity,seller_id,seller_name,dic_produtos_disponiveis,preco):
        novoProduto=Product(product_name,description,fabrication_date,seller_id,seller_name,genre,location,new_product,len(dic_produtos_disponiveis)+1,quantity,preco)
        dic_produtos_disponiveis[novoProduto.product_id]=novoProduto

    def vender(dic_produtos_disponiveis, id_comprador, id_item, dic_user):
        print(f'Você quer vender {dic_produtos_disponiveis[id_item].quantity} para {dic_user[id_comprador].name}, pelo preço de {dic_produtos_disponiveis[id_item].quantity*dic_produtos_disponiveis[id_item].preco}?')
        venda=input("(S/N): ").upper()
        if venda=='S':
            return True
        else:
            return False
#não foi implementado
    def editarPerfil():
        pass