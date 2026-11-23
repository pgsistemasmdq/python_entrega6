"""Funciones de presentación de los posts en la consola.

Las búsquedas y los filtros ahora son métodos de Blog, en modelos.py.
"""


def listar_posts(lista):
    if not lista:
        print("No hay publicaciones para mostrar.")
        return

    for post in lista:
        titulo = post.titulo if isinstance(post.titulo, str) and post.titulo.strip() else "Sin título"
        nombre = post.autor.nombre if isinstance(post.autor.nombre, str) and post.autor.nombre.strip() else "Autor desconocido"
        estado = post.estado if isinstance(post.estado, str) and post.estado.strip() else "Sin estado"
        print(f"- {titulo} | Autor: {nombre} | Estado: {estado}")
