import sqlite3

class FilmeRepository:

    def salvar(self, filme):

        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS filme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            duracao INTEGER,
            genero TEXT,
            diretor TEXT,
            elenco TEXT
        )
        """)

        cursor.execute("""
        INSERT INTO filme
        (titulo, duracao, genero, diretor, elenco)
        VALUES (?, ?, ?, ?, ?)
        """, (
            filme.titulo,
            filme.duracao,
            filme.genero,
            filme.diretor,
            filme.elenco
        ))

        conexao.commit()
        conexao.close()
