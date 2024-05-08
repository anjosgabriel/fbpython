class Conta:
    def __init__(self, numero, cpf, saldo=0.0, ativo=True):
        self.numero = numero
        self.cpf = cpf
        self._saldo = saldo
        self.ativo = ativo


    def get_saldo(self):
        return self._saldo


    def ativar(self):
        self.ativo = True


    def _debito(self, valor):
        if valor < 0:
            raise ValueError("Não é possível debitar, pois o valor é negativo!")
        if self._saldo >= valor:
            self._saldo -= valor
        else:
           raise ValueError("Saldo insuficiente.")


    def credito(self, valor):
        if valor < 0:
            raise ValueError("Não é possível creditar, pois o valor é negativo!")
        self._saldo += valor


    def debito(self, valor):
        self._debito(valor)


    def extrato(self):
        print("Extrato da Conta:")
        print(f"Saldo: R${self.get_saldo():.2f}")