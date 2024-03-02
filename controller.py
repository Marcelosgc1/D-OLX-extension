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
    pedido_aceito=pedido_aceito=computada=False
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
        if Persistency.get_instance().get_produtos_disponiveis()[i].genre==pesquisa or Persistency.get_instance().get_produtos_disponiveis()[i].product_name==pesquisa:
            lista_pesquisa.append(Persistency.get_instance().get_produtos_disponiveis()[i])
    for i in lista_pesquisa:
        print(f'{i.product_name}, {i.description}, data de fabricação do produto: {i.fabrication_date}, localização do produto: {i.location}, quantidade disponível: {i.quantity}, por {i.preco}R$', end=', ')
        if i.new_product:
            print('produto novo.')
        else:
            print('produto usado.')
        print(f'ID do produto: {i.product_id}')

def checarComentarios(id):
    dic_dos_produtos=Persistency.get_instance().get_produtos_disponiveis()
    if dic_dos_produtos.get(id)!=None:
        for i in dic_dos_produtos[id].comments:
            print(dic_dos_produtos[id].comments[i])




###mostrar no video
#persistencia=Persistency.get_instance()
#cadastrarUsuario('joao',21,1,12345678,'joao@gmail.com','joaosecreto')
#cadastrarUsuario('joao',21,1,12345678,'joao@gmail.com','joaosecreto')
#cadastrarUsuario('pedro',19,2,87654321,'pedro@gmail.com','pedrosecreto')
#input()
#fusquinha=Seller.criarEPublicarProduto('carro','fusca',1988,'automovel','feira de santana', False, 1, 2, 30000)
#Seller.criarEPublicarProduto('carro','onix',2024,'automovel','feira de santana', True, 1, 1, 100000)
#Seller.criarEPublicarProduto('volta ao mundo em 80 dias', 'livro de julio verne, capa dura', 2012, 'livro', 'feira de santana', 'False', 2, 1, 20)
#if fusquinha:
#    print('criado!')
#    input()
#buscarProduto('carro')
#input()
#realizarVenda(persistencia.get_produtos_disponiveis()[2], persistencia.get_usuarios()[2][0], persistencia.get_usuarios()[1][1], 1)
#input()
#realizarVenda(persistencia.get_produtos_disponiveis()[2], persistencia.get_usuarios()[2][0], persistencia.get_usuarios()[1][1], 1)
#input()
#persistencia.get_usuarios()[1][0].realizarComentario(persistencia.get_produtos_disponiveis()[3])
#input()
#realizarVenda(persistencia.get_produtos_disponiveis()[3], persistencia.get_usuarios()[1][0], persistencia.get_usuarios()[2][1], 1)
#input()
#persistencia.get_usuarios()[1][0].realizarComentario(persistencia.get_produtos_disponiveis()[3])
#checarComentarios(3)