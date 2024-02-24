from models.Buyer import Buyer
from models.Seller import Seller
from Persistency.persistency import Persistency

persistencia=Persistency()

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



def cadastrarUsuario(dicionario_de_usuarios, nome, idade, id):
    if dicionario_de_usuarios.get(id)!=None:
        novoUsuarioCompra=Buyer(nome, idade, id)
        novoUsuarioVenda=Seller(nome, idade, id)
        dicionario_de_usuarios[id]=(novoUsuarioCompra, novoUsuarioVenda)
        persistencia.dicionario_usuarios=dicionario_de_usuarios
        print(f'Usuário {nome} cadastrado com sucesso')
        return True
    else:
        print('Já existe um usuário cadastrado com esse CPF')
        return False
    