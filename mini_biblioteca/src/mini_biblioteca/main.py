from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo

usuario = Usuario(nome="Robson", id_usuario="1")
livro = Livro("Harry Potter", "J.K", "1")
print(f"Disponibilidade do livro após criação: {livro.disponivel}")
emprestimo = Emprestimo(livro, usuario)
print(f"Disponibilidade do livro após empréstimo: {livro.disponivel}")
print(f"Estado do empréstimo após criação: {emprestimo.ativo}")
emprestimo.devolver()
print(f"Disponibilidade do livro após devolução: {livro.disponivel}")
print(f"Estado do empréstimo após devolucão: {emprestimo.ativo}")

