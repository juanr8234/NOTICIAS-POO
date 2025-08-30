class Noticia:
    def __init__(self, titulo: str, categoria: str, cuerpo: str):
        self.titulo = titulo
        self.categoria = categoria
        self.cuerpo = cuerpo  # puede ser texto, imágenes o videos en una implementación futura

    def __str__(self):
        return f"[{self.categoria.upper()}] {self.titulo}"