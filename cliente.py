class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
        
    @property    
    def batata(self):
        return self.__nome.title() 
    
    @batata.setter
    def chinelo(self, nome):
        self.__nome = nome   