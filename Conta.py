class Conta:
    def __init__(self, titular, saldo):
        
        self._saldo = 0
        self._titular = titular


    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if (saldo<0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if (self._saldo>= valor):
            self._saldo-= valor
            print("Saque realizado com sucesso")
        else:
            print("saldo insuficiente")

    def deposita(self, valor):
        self._saldo+= valor
        print("Depósito realizado")

    def extrato(self):
        print("Cliente: ", self._titular, "Saldo atual: ", self._saldo)