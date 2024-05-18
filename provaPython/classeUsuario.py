class Usuario:
    def __init__(self, id_usuario, nome, login, senha):
        self.id_usuario = id_usuario
        self.nome = nome
        self.login = login
        self.senha = senha

    def __str__(self):
        return f'Usuario(id_usuario={self.id_usuario}, nome={self.nome}, login={self.login}, senha={self.senha})'

    def set_senha(self, nova_senha):
        self.senha = nova_senha

    def autenticar(self, login, senha):
        return self.login == login and self.senha == senha