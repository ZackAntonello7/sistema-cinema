class FilmeService:

    def __init__(self, repository):
        self.repository = repository

    def cadastrar_filme(self, filme):

        if filme.titulo == "":
            raise Exception("Título inválido")

        self.repository.salvar(filme)
