from src.model.filme import Filme

class FilmeController:

    def __init__(self, service):
        self.service = service

    def cadastrar(self, dados):

        filme = Filme(
            dados["titulo"],
            dados["duracao"],
            dados["genero"],
            dados["diretor"],
            dados["elenco"]
        )

        self.service.cadastrar_filme(filme)

        print("Filme cadastrado com sucesso")
