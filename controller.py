from models.Buyer import Buyer
from models.Seller import Seller
from models.Product import Product
from models.persistency import Persistency



def converter_cpf(cpf):
    while True:
        try:
            cpf=int(cpf.strip().replace('.','').replace('-',''))
            if len(str(cpf))==11:
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


###principal
persistencia=Persistency.get_instace()

menu1=1
menu2=1
#não foi implementado a main/arq principal
while menu1==1:
    x=input("Bem vindo, quer se cadastrar ou fazer login? (C/L)")
    if x.upper()=='C':
        nome=input('nome: ')
        idade=int(input('idade: '))
        cpf=converter_cpf(input('cpf (XXX.XXX.XXX-XX): '))
        telefone=int(input('telefone: '))
        email=input('email: ')
        senha=input('senha: ')
        cadastrarUsuario(persistencia.get_usuarios(),nome,idade,cpf,telefone,email,senha)
    elif x.upper()=='L':
        cpf=converter_cpf(input('insira seu cpf: '))
        senha=input('senha: ')
        if persistencia.get_usuarios().get(cpf)==None:
            print('Esse usuario não foi cadastrado.')
        elif persistencia.get_usuarios().get(cpf)[0].password!=senha:
            print('Senha errada.')
        else:
            print(f"Bem vindo {persistencia.get_usuarios().get(cpf)[0].nome}!")
