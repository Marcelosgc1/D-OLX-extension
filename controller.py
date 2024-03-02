from models.Buyer import Buyer
from models.Seller import Seller
from models.Product import Product
from models.persistency import Persistency
from models.UsersFactory import User_Factory


def cadastrarUsuario(nome, idade, id:int, telefone, email, senha):
    novoUsuarioCompra=User_Factory.criar_Usuario(nome, idade, id, telefone, email, senha, 'Buyer')
    novoUsuarioVenda=User_Factory.criar_Usuario(nome, idade, id, telefone, email, senha, 'Seller')
    if novoUsuarioCompra==False or novoUsuarioVenda==False:
        print('Falha na criação do usuário, tente novamente')
        return False
    
    Persistency.get_instance().set_novo_user(id, novoUsuarioCompra, novoUsuarioVenda)
    print(f'Usuário {nome} cadastrado com sucesso')
    return True
    
def computarVenda(id_item:int, qnt:int):
    if Persistency.get_instance().get_produtos_vendidos().get(id_item)==None:
        Persistency.get_instance().get_produtos_vendidos()[id_item]=0
    Persistency.get_instance().set_quantidade_disponiveis(id_item,-qnt)
    Persistency.get_instance().set_quantidade_vendidos(id_item,qnt)
    return True

def realizarVenda(produto:Product,comprador:Buyer,vendedor:Seller, qnt_comprar:int):
    pedido_realizado=comprador.comprar(produto, qnt_comprar)
    if pedido_realizado:
        pedido_aceito=vendedor.vender(produto, comprador)
    if pedido_aceito:
        comprador.comprados.append(produto.product_id)
        computada=computarVenda(produto.product_id, qnt_comprar)
    if computada:
        print('Venda realizada com sucesso!')
        return True
    

def buscarProduto(pesquisa):
    lista_pesquisa=[]
    for i in Persistency.get_instance().get_produtos_disponiveis():
        if Persistency.get_instance().get_produtos_disponiveis()[i].genre==pesquisa or Persistency.get_instance().get_produtos_disponiveis()[i].nome==pesquisa:
            lista_pesquisa.append(Persistency.get_instance().get_produtos_disponiveis()[i])
    for i in lista_pesquisa:
        print(f'{i.product_name}, {i.description}, data de fabricação do produto: {i.fabrication_date}, localização do produto: {i.location}, quantidade disponível:{i.quantity}, por {i.preco}R$', end='')
        if i.new_product:
            print('produto usado.')
        else:
            print('produto novo.')
        print(f'ID do produto: {i.product_id}')

def checarComentarios(id):
    dic_dos_produtos=Persistency.get_instance().get_produtos_disponiveis()
    if dic_dos_produtos.get(id)!=None:
        for i in dic_dos_produtos[id].comments:
            print(dic_dos_produtos[id].comments[i])


###mostrar no video
#cadastrarUsuario('joao',21,1,12345678,'joao@gmail.com','joaosecreto')
#cadastrarUsuario('joao',21,1,12345678,'joao@gmail.com','joaosecreto')
