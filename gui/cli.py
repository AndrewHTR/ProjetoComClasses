from modules.cliente import Cliente
from modules.conta import Conta
import os
size = os.get_terminal_size()
class Gui(Cliente):
    def __init__(self, nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
        
    @classmethod
    def pegarInfo(self):
        
        
        print(size.columns * '*')
        nome = input('Digite seu nome: ')
        sobrenome = input('Digite seu sobrenome: ')
        cpf = input('Digite seu cpf: ')
        print(size.columns * '*')
        print('')
        return self(nome,sobrenome,cpf)
    def mostrarInfo(self):
        print(size.columns * '*')
        print(f'Seu nome é: {self.nome}, Sobrenome: {self.sobrenome} e seu cpf é: {self.cpf}')
