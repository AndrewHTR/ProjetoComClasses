import modules.conta as minhaConta
import modules.cliente as meuCliente
import gui.cli as minhaGui

cliente1 = minhaConta.Cliente('Andrew', 'Silva', '11111111-1')
cliente2 = minhaConta.Cliente('Luisa','Souza','123232323-2')
conta = minhaConta.Conta('3123', cliente1.nome,cliente1.sobrenome,cliente1.cpf, 500,10000)
conta2 = minhaConta.Conta('2323',cliente2.nome,cliente2.sobrenome,cliente2.cpf,500,10000)
"""print(conta.nome)
print(conta.numero)
print(conta.nome)
conta.deposita(423)
print(conta.nome)
conta.saca(500)
conta.transfere_para(conta2, 400)
conta.transfere_para(conta2,2)
conta2.transfere_para(conta,2)
conta2.extrato
conta.extrato
print(conta2.nome)
print(conta.nome)
conta.historico.imprime()"""
continua = minhaGui.Gui.iniciarGui()
