from models.noticia import Noticia

class BuscadorNoticias:
    def __init__(self, noticias):
        self.noticias = noticias

    def buscar_por_titulo(self, texto):
        """Busca noticias cuyo título contenga el texto indicado"""
        return [n for n in self.noticias if texto.lower() in n.titulo.lower()]

    def buscar_por_categoria(self, categoria):
        """Busca noticias de una categoría específica"""
        return [n for n in self.noticias if n.categoria.lower() == categoria.lower()]

    def buscar_por_palabra(self, palabra):
        """Busca noticias cuyo cuerpo contenga una palabra"""
        return [n for n in self.noticias if palabra.lower() in n.cuerpo.lower()]

    def buscar_por_lista_palabras(self, lista_palabras):
        """Busca noticias cuyo cuerpo contenga todas las palabras dadas"""
        return [
            n for n in self.noticias
            if all(p.lower() in n.cuerpo.lower() for p in lista_palabras)
        ]

    def buscar_por_max_palabras(self, max_palabras):
        """Busca noticias cuyo cuerpo tenga un número de palabras menor o igual al límite"""
        return [
            n for n in self.noticias
            if len(n.cuerpo.split()) <= max_palabras
        ]

    def buscar_combinado(self, titulo=None, categoria=None, palabra=None, lista_palabras=None, max_palabras=None):
        """Permite combinar filtros en una sola búsqueda"""
        resultados = self.noticias

        if titulo:
            resultados = [n for n in resultados if titulo.lower() in n.titulo.lower()]

        if categoria:
            resultados = [n for n in resultados if n.categoria.lower() == categoria.lower()]

        if palabra:
            resultados = [n for n in resultados if palabra.lower() in n.cuerpo.lower()]

        if lista_palabras:
            resultados = [n for n in resultados if all(p.lower() in n.cuerpo.lower() for p in lista_palabras)]

        if max_palabras:
            resultados = [n for n in resultados if len(n.cuerpo.split()) <= max_palabras]

        return resultados
