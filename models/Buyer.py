from models.User import User
from models.persistency import Persistency
from models.Seller import Seller

class Buyer(User):
    def __init__(self, name:str, age:int, id:int, phone:int, email:str, password:str):
        self.name=name
        self.age=age
        if id in Persistency.get_instace().get_usuarios():
            return False
        self.id=id
        self.phone=phone
        self.email=email
        self.password=password

    def buscarProduto(pesquisa, dic):
        lista_pesquisa=[]
        for i in dic:
            if dic[i].genre==pesquisa or dic[i].nome==pesquisa:
                lista_pesquisa.append(dic[i])
        for i in lista_pesquisa:
            print(f'{i.product_name}, {i.description}, data de fabricação do produto: {i.fabrication_date}, localização do produto: {i.location}, quantidade disponível:{i.quantity}, por {i.preco}', end='')
            if i.new_product:
                print('produto usado.')
            else:
                print('produto novo.')
            print(f'ID do produto: {i.product_id}')

    def comprar(id_item, dic_produtos_disponiveis, quantidade_comprar, id_comprador, dic_usuarios):
        if dic_produtos_disponiveis[id_item].quantity==0:
            print('Esse produto não está disponivel no momento')
            return False
        elif dic_produtos_disponiveis[id_item].quantity<quantidade_comprar:
            print(f"Esse produto tem apenas {dic_produtos_disponiveis[id_item].quantity} exemplares.")
            return False
        print(f"O produto é: {dic_produtos_disponiveis[id_item].product_name}; {dic_produtos_disponiveis[id_item].description}")
        confirmacao=input('Tem certeza que esse é o produto que você quer comprar? (S/N): ').upper()
        if confirmacao!='S':
            print('compra encerrada')
            return False
        else:
            realizado=Seller.vender(dic_produtos_disponiveis, id_comprador, id_item, dic_usuarios)
        if realizado:
            return realizado
        else:
            print('compra recusada')
#não foi implementado        
    def editarPerfil():
        pass
#não foi implementado
    def permitirNotificacoes():
        pass