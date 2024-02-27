from models.User import User
from models.persistency import Persistency

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
            print(f'{i.product_name}, {i.description}, data de fabricação do produto: {i.fabrication_date}, localização do produto: {i.location}, quantidade disponível:{i.quantity}, ', end='')
            if i.new_product:
                print('produto usado.')
            else:
                print('produto novo.')
            print(f'ID do produto: {i.product_id}')

    def comprar():
        pass

    def editarPerfil():
        pass

    def permitirNotificacoes():
        pass