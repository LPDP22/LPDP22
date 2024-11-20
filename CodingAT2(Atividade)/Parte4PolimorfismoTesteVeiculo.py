from Parte3HerancaCarro import Carro
from Parte3HerancaMoto import Moto
from Parte5Composicao import Motor

def teste_veiculo(veiculo):
    veiculo.acelerar()
    veiculo.acelerar()
    print(f'{veiculo.mostrar_velocidade()} km/h\n')
    veiculo.frear()
    print(f'{veiculo.mostrar_velocidade()} km/h\n')

carro = Carro('Fiat', 'Uno', Motor('73 CV'))
print(f"Dados(Carro): {carro.getMarca()}, {carro.getModelo()}, {carro.getMotor()}")
teste_veiculo(carro)

moto = Moto('Honda', 'CG202')
print(f"Dados(Moto): {moto.getMarca()}, {moto.getModelo()}")
teste_veiculo(moto)