from src.repository.filme_repository import FilmeRepository
from src.service.filme_service import FilmeService
from src.controller.filme_controller import FilmeController

dados = {
    "titulo": "Batman",
    "duracao": 120,
    "genero": "Ação",
    "diretor": "Matt Reeves",
    "elenco": "Robert Pattinson"
}

repository = FilmeRepository()
service = FilmeService(repository)
controller = FilmeController(service)

controller.cadastrar(dados)
