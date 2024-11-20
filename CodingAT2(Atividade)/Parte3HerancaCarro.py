from Parte2AbstraçãoVeículo import Veiculo
from Parte5Composicao import Motor

class Carro(Veiculo):

    def __init__(self, modelo, marca, motor: Motor):
        super().__init__(modelo, marca)
        self.__motor = motor
    
    #Implementação da classe abstrata
    #Aumento de velocidade por 10 km/h
    def acelerar(self):
        self._velocidade += 10
    
    #Redução de velocidade por 10 km/h
    def frear(self):
        self._velocidade -= 10
        if self._velocidade < 0:
            self._velocidade = 0
            
    #Para que a velocidade seja mostrada       
    def mostrar_velocidade(self):
        return self._velocidade
    
    #Adquirir a potência do motor        
    def getMotor(self):
        return self.__motor.getPotencia()