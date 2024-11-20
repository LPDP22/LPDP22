class BancoLucas:
    def __init__(self, titular, numero_conta):
        # '__' faz com que os atributos fiquem privados
        self.__titular = titular
        self.__numeroconta = numero_conta
        #Isso faz com que o saldo não possa ser alterado fora dessa classe.
        self.__saldo = 0
    
    def getNumeroconta(self):
        return self.__numeroconta
    
    def getTitular(self):
        return self.__titular
    
    #Função para consultar o saldo
    def getSaldo(self):
        return self.__saldo
    
    def setNumeroconta(self, numero_conta):
        return self.__numeroconta == numero_conta
    
    def setTitular(self, titular):
        return self.__titular == titular
    
    #Função para sacar valor da conta
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de {valor} efetuado com sucesso")
        else:
            print('Saque insuficiente')
    
    #Função para depositar na conta
    def depositar(self, valor):
        self.__saldo += valor
    
    #Função para consultar o saldo
    def consultaSaldo(self):
        return self.__saldo
    
objeto = BancoLucas('1','Lucas')
print(f'Nº de Conta: {objeto.getNumeroconta()}\nTitular: {objeto.getTitular()}\nSaldo: {objeto.getSaldo()}')

objeto.depositar(100.10)
print(f'Foi depositado R$ 100.10. Saldo atual: {objeto.getSaldo}')

objeto.sacar(5.00)
print(f'Foi sacado R$5.00 da conta. Saldo atual: {objeto.getSaldo}')

print("Alterando Conta de Usuario")
objeto.setTitular('Lucas Paulo')
objeto.setNumeroconta('23')
print(f'Alterados com sucesso!\nNº de Conta: {objeto.getNumeroconta}\nNome de Titular: {objeto.getTitular}')