from Parte2AbstraçãoVeículo import Veiculo

class Moto(Veiculo):
    
    def __init__(self, modelo, marca):
        super().__init__(modelo, marca)
    
    #Implementação da classe abstrata
    #Aumento de velocidade por 15 km/h
    def acelerar(self):
        self._velocidade += 15
    
    #Redução de velocidade por 10 km/h
    def frear(self):
        self._velocidade -= 10
        if self._velocidade < 0:
            self._velocidade = 0
    
    #Para que a velocidade seja mostrada
    def mostrar_velocidade(self):
        return self._velocidade