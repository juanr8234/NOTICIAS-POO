import pytest
from models.noticia import Noticia
from models.usuario import Usuario
from models.suscripcion import Suscripcion
from services.servidor import ServidorNoticias
from services.buscador import BuscadorNoticias


def test_suscripcion_por_categoria_y_palabra():
    servidor = ServidorNoticias()
    usuario = Usuario("Juan")
    suscripcion = Suscripcion(categoria="deportes", palabras_clave=["De Paul"])
    usuario.agregar_suscripcion(suscripcion)
    servidor.registrar_usuario(usuario)

    noticia = Noticia("Argentina campeón", "deportes", "Gol de De Paul en la final")
    servidor.agregar_noticia(noticia)

    # Verificar que Juan recibió la noticia
    assert any(sus.cumple(noticia) for sus in usuario.suscripciones)


def test_suscripcion_no_cumple_categoria():
    servidor = ServidorNoticias()
    usuario = Usuario("Ana")
    suscripcion = Suscripcion(categoria="deportes", palabras_clave=["De Paul"])
    usuario.agregar_suscripcion(suscripcion)
    servidor.registrar_usuario(usuario)

    noticia = Noticia("Fiesta en Ibiza", "chimentos", "De Paul disfrutó en la playa")
    servidor.agregar_noticia(noticia)

    # Ana no debería recibir la noticia porque no es de deportes
    assert not any(sus.cumple(noticia) for sus in usuario.suscripciones)


def test_buscador_por_titulo():
    noticia1 = Noticia("Argentina campeón", "deportes", "Texto...")
    noticia2 = Noticia("Nuevo récord de Messi", "deportes", "Texto...")

    buscador = BuscadorNoticias([noticia1, noticia2])

    resultados = buscador.buscar_por_titulo("Messi")

    assert len(resultados) == 1
    assert resultados[0].titulo == "Nuevo récord de Messi"


def test_buscador_por_categoria():
    noticia1 = Noticia("Argentina campeón", "deportes", "Texto...")
    noticia2 = Noticia("Crisis económica", "politica", "Texto...")

    buscador = BuscadorNoticias([noticia1, noticia2])

    resultados = buscador.buscar_por_categoria("deportes")

    assert len(resultados) == 1
    assert resultados[0].categoria == "deportes"
