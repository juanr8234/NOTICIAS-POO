from models.noticia import Noticia
from models.usuario import Usuario
from models.suscripcion import Suscripcion
from services.servidor import ServidorNoticias
from services.buscador import BuscadorNoticias

def main():
    print("=== Sistema de Noticias POO ===")

    # Crear servidor
    servidor = ServidorNoticias()

    # Crear usuario
    usuario1 = Usuario("Juan")

    # Crear suscripción: quiere noticias de deportes que hablen de "De Paul"
    suscripcion_deportes = Suscripcion(categoria="deportes", palabras_clave=["De Paul"])
    usuario1.agregar_suscripcion(suscripcion_deportes)

    # Registrar usuario en el servidor
    servidor.registrar_usuario(usuario1)

    # Crear noticias
    noticia1 = Noticia("Argentina campeón", "deportes", "Argentina ganó la final con un gol de De Paul.")
    noticia2 = Noticia("Fiesta de De Paul en Ibiza", "chimentos", "De Paul disfrutó de una fiesta en la playa.")
    noticia3 = Noticia("Nuevo récord de Messi", "deportes", "Messi rompió otro récord histórico.")

    # Agregar noticias al servidor
    print("\nAgregando noticias al servidor...\n")
    servidor.agregar_noticia(noticia1)
    servidor.agregar_noticia(noticia2)
    servidor.agregar_noticia(noticia3)

    # Búsqueda manual de noticias
    buscador = BuscadorNoticias(servidor.noticias)
    print("\nBuscando noticias con 'Messi':")
    for n in buscador.buscar_por_palabra("Messi"):
        print("-", n)

if __name__ == "__main__":
    main()
