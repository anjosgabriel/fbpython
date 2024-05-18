class Produto:
    def __init__(self,id,codigo,nome,valor,estoque=0):
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.valor  = valor
        self.estoque = estoque 
    
    def incluir(self,valor):
        self.estoque = self.estoque + valor

    def retirar(self, valor):
        if valor <= 0:
            print("impossivel realizar")
        elif valor > self.estoque: 
            print("Sem estoque disponível")
        else:
            self.estoque = self.estoque - valor