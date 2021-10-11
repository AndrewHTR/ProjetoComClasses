import datetime
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today
        self.transacoes = []
    def imprime(self):
        print(f'Data de abertura {self.data_abertura}')
        print('Transações: ')
        for t in self.transacoes:
            print(f'- {t}')

class Cliente:
    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self,numero,titular,saldo,limite):
        self.numero = numero
        self.titular = titular
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
            print(f'Concluido! Sera adicionado {valor} a conta {destino}')
            destino.deposita(valor)
            self.historico.transacoes.append(f'Você transferiu {valor} para {destino}')