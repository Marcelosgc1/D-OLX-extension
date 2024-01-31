class Persistency:
    
    instance = None
    
    @classmethod
    def get_instace(Persistency):
        if not Persistency.instance:
            Persistency.instance=Persistency()
        return Persistency.instance
    #SINGLETON :D