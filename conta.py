import enginee.engine as minhaConta
cliente1 = minhaConta.Cliente('Andrew', 'Silva', '11111111-1')
cliente2 = minhaConta.Cliente('Luisa','Souza','123232323-2')
conta = minhaConta.Conta('3123', cliente1.nome, 500,10000)
conta2 = minhaConta.Conta('2323',cliente2.nome,500,10000)
print(conta.titular)
print(conta.numero)
print(conta)
conta.deposita(423)
print(conta)
conta.saca(500)
conta.transfere_para(conta2, 400)
conta.transfere_para(conta2,2)
conta2.transfere_para(conta,2)
conta2.extrato
conta.extrato
print(conta2)
print(conta.titular)
conta.historico.imprime()