class Conta:
    def __init__(self, titular,numero,saldo):

        self.numero = numero
        self.saldo = 0
        self.titular = titular

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if (saldo<0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo