class Produtolivraria:
    def __init__(self, id_produtolivraria, descricao, editora, valor, estoque):
        self.id_produtolivraria = id_produtolivraria
        self.descricao = descricao
        self.editora = editora
        self.valor = valor
        self.estoque = estoque

    def __str__(self):
        return (f'Produtolivraria(id_produtolivraria={self.id_produtolivraria}, '
                f'descricao={self.descricao}, editora={self.editora}, '
                f'valor={self.valor}, estoque={self.estoque})')

    def atualizar_estoque(self, quantidade, operacao):
        if operacao == 'entrada':
            novo_estoque = self.estoque + quantidade
        elif operacao == 'saida':
            novo_estoque = self.estoque - quantidade
        else:
            raise ValueError("Operação inválida. Use 'entrada' ou 'saida'.")
        
        if novo_estoque < 0 or novo_estoque > 18:
            raise ValueError("Quantidade inválida. O estoque deve estar entre 0 e 18.")
        self.estoque = novo_estoque

    def atualizar_detalhes(self, descricao, editora, valor, estoque):
        self.descricao = descricao
        self.editora = editora
        self.valor = valor
        self.estoque = estoque
