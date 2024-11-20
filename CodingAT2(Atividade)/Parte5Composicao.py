#Classe Motor com o atributo Potencia
class Motor:
    def __init__(self, potencia):
        self.__potencia = potencia
    
    def getPotencia (self):
        return self.__potencia