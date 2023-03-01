class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        
        
    # "__" boa prática para indicar que um atributo é privado, ou seja, não deve ser usado diretamente    
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
        
    def deposita(self, valor):
        self.__saldo += valor    

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)): 
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))      
        
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)    
        
    @property    
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):    
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    # metodos estaticos estao ligados a classe e nao ao objeto  
    @staticmethod  
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}  
                
# conta = Conta(123, "vitor", 55.0, 1000.0)        
# conta2 = Conta(321, "leticia", 76.0, 1000.0)        
