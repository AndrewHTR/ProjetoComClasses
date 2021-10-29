from modules.cliente import *
from modules.conta import *
import os
import random
size = os.get_terminal_size()

class Gui(Conta):
    def __init__(self,numero, nome,sobrenome,cpf,saldo=0,limite=500):
        super().__init__()
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    @classmethod
    def iniciarGui(self):
        escolha = False
        while escolha == False:
            print(size.columns * '*')
            print('')
            nome = input('Digite seu nome: ')
            sobrenome = input('Digite seu sobrenome: ')
            cpf = input('Digite seu cpf: ')
            print('')
            print(size.columns * '*')
            escolha1 = int(input('Errou alguma opção? Digite (1) para refazer ou (0) para continuar\n'))
            if escolha1 == 0:
                break
            print('')
        resposta1 = int(input('Você deseja criar uma conta? 1 para sim e 0 para não: '))
        match resposta1:
            case 1:
                print(size.columns * '*')
                print('Agora criaremos sua conta...\n')
                numerozada = [1,2,3,4,5,6,7,8,9,10,11]
                random.shuffle(numerozada)
                for i in range(len(numerozada)):
                    print(max(numerozada) - numerozada[i], end = ' ')
               

                
        return self
