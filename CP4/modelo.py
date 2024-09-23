class Livro:


    def __init__(self, titulo : str, autor : str, ano : int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"""({autor}), ({titulo}), ({ano})"""