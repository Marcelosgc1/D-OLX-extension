class Persistency:
    
    instance = None
    
    @classmethod
    def get_instace(Persistency):
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
       self.produtos_disponiveis[id]+=mudanca

    def set_quantidade_vendidos(self, id:int, mudanca:int):
        self.produtos_vendidos[id]+=mudanca