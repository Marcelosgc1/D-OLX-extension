from models.User import User
from models.Product import Product
from models.persistency import Persistency

class Seller(User):
    def __init__(self, name:str, age:int, id:int, phone:int, email:str, password:str):
        self.name=name
        self.age=age
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password
        self.meusProdutos=[]
        
    def criarEPublicarProduto(product_name,description,fabrication_date,genre,location,new_product,seller_id,quantity,preco):
        novoProduto=Product(product_name,description,fabrication_date,seller_id,genre,location,new_product,len(Persistency.get_instance().get_produtos_disponiveis())+1,quantity,preco)
        Persistency.get_instance().set_novo_produto(novoProduto.product_id, novoProduto)
        Persistency.get_instance().get_usuarios()[seller_id][1].meusProdutos.append(novoProduto.product_id)
        return True

    def vender(self, produto, comprador):
        print(f'Você quer vender {produto.quantity} {produto.product_name} para {comprador.name}, pelo preço de {produto.quantity*produto.preco}?')
        venda=input("(S/N): ").upper()
        if venda=='S':
            return True
        else:
            return False
        
#não foi implementado
    def editarPerfil():
        pass