class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João","(11) 1111-11111")
conta = Conta(c1., 6546, 0)

print(conta.titular, "Numero:", conta.numero, "Saldo:", conta.saldo)