from Parte3HerancaCarro import Carro
from Parte3HerancaMoto import Moto
from Parte5Composicao import Motor

def teste_veiculo(veiculo):
    #Chamar 'acelerar' duas vezes
    veiculo.acelerar()
    veiculo.acelerar()
    #Mostrar a velocidade
    print(f'{veiculo.mostrar_velocidade()} km/h\n')
    Chamar 'frear' uma vez.
    veiculo.frear()
    #Mostrar a velocidade
    print(f'{veiculo.mostrar_velocidade()} km/h\n')

#Mostrar os dados do carro
carro = Carro('Fiat', 'Uno', Motor('73 CV'))
print(f"Dados(Carro): {carro.getMarca()}, {carro.getModelo()}, {carro.getMotor()}")
teste_veiculo(carro)

#Mostrar os dados de moto
moto = Moto('Honda', 'CG202')
print(f"Dados(Moto): {moto.getMarca()}, {moto.getModelo()}")
teste_veiculo(moto)
