class Suscripcion:
    def __init__(self, categoria=None, palabras_clave=None):
        self.categoria = categoria
        self.palabras_clave = palabras_clave if palabras_clave else []

    def cumple(self, noticia):
        """Evalúa si la noticia coincide con la suscripción"""
        if self.categoria and self.categoria != noticia.categoria:
            return False

        for palabra in self.palabras_clave:
            if palabra.lower() not in noticia.cuerpo.lower() and palabra.lower() not in noticia.titulo.lower():
                return False

        return True
