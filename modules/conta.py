from modules.cliente import Cliente
from modules.historico import Historico

class Conta(Cliente):
    def __init__(self,numero,nome,sobrenome,cpf,saldo,limite):
        super().__init__(nome,sobrenome,cpf)
        self.numero = numero
        self.titular = nome
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self,valor):
        print(f'Sera adicionado {valor} a sua conta!\nVocê tem: {self.saldo+valor} restantes.')
        self.saldo += valor
        self.historico.transacoes.append(f'Você depositou: {valor}')

    def saca(self,valor):
        if (valor > self.saldo):
            print('Ação falhada! Você não tem o bastante para sacar.')
            return False
        else:
            print(f'Ação concluida! Sera descontado {valor} do seu saldo.\nVocê tem: {self.saldo-valor} restantes. ')
            self.saldo -= valor
            self.historico.transacoes.append(f'Você sacou: {valor}')
            return True

    def extrato(self):
        print(f'Numero: {self.numero} Saldo: {self.saldo}')
       

    def transfere_para(self,destino,valor):
        retirou = self.saca(valor)
        if self.saldo < valor:
            print('Ação falha! Você não tem a quantia pedida.')
        else:
            print(f'Concluido! Sera adicionado {valor} a conta {destino.nome}')
            destino.deposita(valor)
            self.historico.transacoes.append(f'Você transferiu {valor} para {destino.nome}')