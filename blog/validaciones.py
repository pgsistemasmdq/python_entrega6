"""Validaciones de los objetos Post, utilizadas al crear y revisar posts."""

from blog.datos import estados_post
from blog.modelos import Autor, Post


def validar_post(post):
    if not isinstance(post, Post):
        return False, "La publicación debe ser un objeto Post"

    if not isinstance(post.id, int) or isinstance(post.id, bool) or post.id <= 0:
        return False, "El ID debe ser un número entero positivo"

    if not isinstance(post.titulo, str) or not post.titulo.strip():
        return False, "El título está vacío o es incorrecto"

    if post.contenido is None:
        return False, 'Falta la clave "contenido"'

    if not isinstance(post.contenido, str) or not post.contenido.strip():
        return False, "El contenido está vacío o es incorrecto"

    if not isinstance(post.autor, Autor):
        return False, "El autor debe ser un objeto Autor"

    if not isinstance(post.autor.nombre, str) or not post.autor.nombre.strip():
        return False, "Falta el nombre del autor o está vacío"

    if not isinstance(post.tags, list):
        return False, "Los tags deben estar en una lista"

    for etiqueta in post.tags:
        if not isinstance(etiqueta, str) or not etiqueta.strip():
            return False, "Los tags deben contener textos no vacíos"

    if not isinstance(post.estado, str) or post.estado not in estados_post:
        return False, "El estado no es válido"

    return True, ""


def validar_todos_los_posts(posts):
    print("\n--- VALIDACIÓN DE POSTS ---")
    if not posts:
        print("No hay publicaciones para validar.")
        return

    for post in posts:
        es_valido, mensaje = validar_post(post)
        identificador = post.id if isinstance(post, Post) else "desconocido"
        if es_valido:
            print(f"Post {identificador}: válido")
        else:
            print(f"Post {identificador}: error - {mensaje}")
