# 📰 Proyecto POO - Servidor de Noticias

Este proyecto implementa un sistema orientado a objetos para gestionar un **servidor de noticias**, permitiendo:

- Registrar noticias provenientes de diferentes agencias.
- Clasificarlas por categorías (deportes, sociales, policiales, etc.).
- Almacenar distintos tipos de contenido (texto, imágenes, videos).
- Realizar búsquedas avanzadas por título, categoría, palabras clave o combinaciones de ellas.
- Gestionar suscripciones de usuarios en base a sus preferencias.
- Notificar automáticamente a los usuarios cuando se publica una noticia que cumple con sus criterios.

---

## 📂 Estructura del proyecto

noticias-POO/
│
├── src/
│ ├── models/
│ │ ├── noticia.py # Clase Noticia
│ │ ├── usuario.py # Clase Usuario
│ │ ├── suscripcion.py # Clase Suscripcion
│ │ 
│ │
│ ├── services/
│ │ ├── servidor.py # Clase ServidorNoticias
│ │ ├── buscador.py # Clase BuscadorNoticias
│ │ └── init.py
│ │
│ └── main.py # Punto de entrada al sistema
│
├── test_noticias.py # Tests automáticos con pytest
│
├── REQUIERE INSTALAR PYTEST PARA EJECUTAR LAS PRUEBAS.
├──pip install pytest / abren cmd en la carpeta noticias-poo/ y ejecutan "pytest -v"
├──
└── README.md # Documentación