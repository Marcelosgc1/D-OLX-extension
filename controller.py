from models.Buyer import Buyer
from models.Seller import Seller
from models.Product import Product
from models.persistency import Persistency

persistencia=Persistency.get_instace()

def converter_cpf(cpf):
    while True:
        try:
            cpf=int(cpf.strip().replace('.','').replace('-',''))
            if len(str(cpf))==9:
                return cpf
        except:
            print('Você não inseriu seu CPF corretamente, tente de novo')
            cpf=input("insira seu cpf novamente: (XXX.XXX.XXX-XX): ")
        else:
            print('Você não inseriu seu CPF corretamente, tente de novo')
            cpf=input("insira seu cpf novamente: (XXX.XXX.XXX-XX): ")



def cadastrarUsuario(dicionario_de_usuarios:dict, nome:str, idade:int, id:int, telefone:int, email:str, senha:str):
    novoUsuarioCompra=Buyer(nome, idade, id, telefone, email, senha)
    novoUsuarioVenda=Seller(nome, idade, id, telefone, email, senha)
    if not novoUsuarioCompra or not novoUsuarioVenda:
        print('Falha na criação do usuário, tente novamente')
        return False
    dicionario_de_usuarios[id]=(novoUsuarioCompra, novoUsuarioVenda)
    persistencia.dicionario_usuarios=dicionario_de_usuarios
    print(f'Usuário {nome} cadastrado com sucesso')
    return True
    
def computarVenda(id_item:int, qnt:int):
    persistencia.set_quantidade_disponiveis(id_item,-qnt)
    persistencia.set_quantidade_vendidos(id_item,qnt)
    return True
