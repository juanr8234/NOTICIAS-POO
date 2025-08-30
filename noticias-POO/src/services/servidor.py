from models.usuario import Usuario
from models.noticia import Noticia

class ServidorNoticias:
    def __init__(self):
        self.noticias = []
        self.usuarios = []

    def agregar_noticia(self, noticia: Noticia):
        self.noticias.append(noticia)
        self._notificar_usuarios(noticia)

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def _notificar_usuarios(self, noticia: Noticia):
        """Verifica si algún usuario debe recibir la noticia"""
        for usuario in self.usuarios:
            for sus in usuario.suscripciones:
                if sus.cumple(noticia):
                    usuario.recibir_noticia(noticia)
