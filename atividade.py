class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self._matricula = matricula
        self._livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self._livros_emprestados) < 3:
            self._livros_emprestados.append(livro)
            livro.set_disponivel(False)
            print(f"Livro '{livro.get_titulo()}' emprestado com sucesso!")
        else:
            print("Limite de empréstimos atingido.")

    def devolver_livro(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)
            livro.set_disponivel(True)
            print(f"Livro '{livro.get_titulo()}' devolvido com sucesso!")
        else:
            print("Você não possui este livro emprestado.")

    def get_livros_emprestados(self):
        return self._livros_emprestados

class Administrador(Pessoa):
    def cadastrar_livro(self, livro):
        print(f"Livro '{livro.get_titulo()}' cadastrado com sucesso!")

    def cadastrar_usuario(self, usuario):
        print(f"Usuário '{usuario.get_nome()}' cadastrado com sucesso!")

class ItemBiblioteca:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor)
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def get_ano_publicacao(self):
        return self._ano_publicacao

    def set_disponivel(self, status):
        self._disponivel = status

    def get_disponivel(self):
        return self._disponivel

# Exemplo de uso
livro1 = Livro("talvez a sua jornada agora seja só sobre você: crônicas", "Iandê Albuquerque", 2022)
livro2 = Livro("A princesa salva a si mesma neste livro", "Amanda Lovelace", 2016)
usuario1 = UsuarioComum("Joaquim", 28, 33333)
administrador1 = Administrador("Maria", 30)

administrador1.cadastrar_livro(livro1)
administrador1.cadastrar_livro(livro2)
administrador1.cadastrar_usuario(usuario1)

usuario1.emprestar_livro(livro1)
usuario1.emprestar_livro(livro2)
usuario1.devolver_livro(livro1)

print(f"Livros disponíveis: {livro1.get_disponivel()}, {livro2.get_disponivel()}")
print(f"Livros emprestados por Joaquim: {usuario1.get_livros_emprestados()}")
