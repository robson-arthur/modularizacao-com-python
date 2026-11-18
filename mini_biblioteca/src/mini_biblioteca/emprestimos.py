from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        self.livro = livro
        self.usuario = usuario
        self.ativo = True

    @property
    def livro(self):
        return self._livro    

    @livro.setter
    def livro(self, novo: Livro):
        if novo.disponivel == False:
            raise ValueError
        self._livro = novo
        self._livro.disponivel = False
    
    def devolver(self):
        self.ativo = False
        self._livro.disponivel = True