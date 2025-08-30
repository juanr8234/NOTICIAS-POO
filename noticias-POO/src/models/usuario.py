from models.suscripcion import Suscripcion

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.suscripciones = []  # lista de objetos Suscripcion

    def agregar_suscripcion(self, suscripcion: Suscripcion):
        self.suscripciones.append(suscripcion)

    def recibir_noticia(self, noticia):
        """Cuando una noticia cumple con sus preferencias"""
        print(f"📩 {self.nombre} recibió la noticia: {noticia}")
