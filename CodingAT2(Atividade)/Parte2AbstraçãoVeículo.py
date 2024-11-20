#Utilizando o módulo abc para implementar a classe abstrata.
from abc import ABC, abstractmethod

#Criando um classe abstrata Veiculo com os métodos abstratos:
class Veiculo(ABC):
    
    def __init__(self, modelo, marca):
        self.__modelo = modelo
        self.__marca = marca
        self._velocidade = 0

    def getModelo (self):
        return self.__modelo
    
    def getMarca (self):
        return self.__marca
    
    #Metodo Abstrato 'acelerar' não implementado na classe Veiculo
    @abstractmethod
    def acelerar(self):
        pass
    
    #Metodo Abstrato 'frear' não implementado na classe Veiculo
    @abstractmethod
    def frear(self):
        pass
    
        #Metodo Abstrato 'mostrar_velocidade' não implementado na classe Veiculo
    @abstractmethod
    def mostrar_velocidade(self):
        pass