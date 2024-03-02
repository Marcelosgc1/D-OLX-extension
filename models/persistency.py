class Persistency:
    
    instance = None
    
    @classmethod
    def get_instance(Persistency):
        if not Persistency.instance:
            Persistency.instance=Persistency()
        return Persistency.instance
    #SINGLETON :D

    def __init__(self):
        self.produtos_disponiveis={}
        self.produtos_vendidos={}
        self.dicionario_usuarios={}

    def get_usuarios(self):
        return self.dicionario_usuarios
    
    def get_produtos_vendidos(self):
        return self.produtos_vendidos
    
    def get_produtos_disponiveis(self):
        return self.produtos_disponiveis
    
    def set_quantidade_disponiveis(self, id:int, mudanca:int):
        self.produtos_disponiveis[id].quantity+=mudanca

    def set_quantidade_vendidos(self, id:int, mudanca:int):
        self.produtos_vendidos[id]+=mudanca
    
    def set_novo_produto(self, id:int, produto:object):
        self.produtos_disponiveis[id]=produto
    
    def set_produto_vendido(self, id:int, qnt_produto:int):
        self.produtos_vendidos[id]=qnt_produto
    
    def set_novo_user(self, id, buyer:object, seller:object):
        self.dicionario_usuarios[id]=(buyer,seller)