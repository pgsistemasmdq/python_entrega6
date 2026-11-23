"""Carga y guardado de publicaciones en un archivo JSON."""

import json
from pathlib import Path

from blog.modelos import Autor, Post

# Conservamos las etiquetas y los estados usados en las entregas anteriores.
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "AI", "Data Science", "Machine Learning", "Pandas", "Deep Learning"}

# El archivo se encuentra junto a main.py, incluso si se ejecuta desde otro lugar.
RUTA_POSTS = Path(__file__).resolve().parent.parent / "posts.json"


def cargar_posts(ruta=RUTA_POSTS):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("No se encontró posts.json. El blog comienza sin publicaciones.")
        return []
    except (json.JSONDecodeError, UnicodeError):
        print("Error: posts.json está vacío o contiene JSON inválido.")
        return []
    except OSError as error:
        print(f"No se pudo leer posts.json: {error}")
        return []

    if not isinstance(datos, list):
        print("Error: posts.json debe contener una lista de publicaciones.")
        return []

    posts = []
    for numero, dato in enumerate(datos, start=1):
        if not isinstance(dato, dict):
            print(f"Post {numero}: se omitió porque no es un diccionario.")
            continue

        datos_autor = dato.get("autor")
        if not isinstance(datos_autor, dict):
            # Un post exige un Autor; no podemos construirlo con otro tipo.
            print(f"Post {numero}: se omitió porque el autor no es un diccionario.")
            continue

        autor = Autor(
            datos_autor.get("nombre", ""),
            datos_autor.get("bio", ""),
            datos_autor.get("especialidad", ""),
            datos_autor.get("redes_sociales", []),
        )
        post = Post(
            dato.get("id", 0),
            dato.get("titulo", ""),
            dato.get("contenido"),  # None permite detectar la clave ausente.
            autor,
            dato.get("tags", []),
            dato.get("estado", ""),
            dato.get("categoria", ""),
        )
        posts.append(post)

    return posts


def guardar_posts(posts, ruta=RUTA_POSTS):
    try:
        # JSON solo admite tipos básicos, por eso convertimos cada Post.
        lista_diccionarios = [post.a_diccionario() for post in posts]
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            archivo.write("\n")
        return True
    except (OSError, TypeError, ValueError) as error:
        print(f"No se pudieron guardar los posts: {error}")
        return False
