"""Punto de entrada de la Preentrega 6 del blog."""

from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.modelos import Autor, Blog, Post
from blog.operaciones import listar_posts
from blog.validaciones import validar_post, validar_todos_los_posts


def main():
    # Al iniciar se convierten los diccionarios del JSON en objetos Post.
    blog = Blog(cargar_posts())

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            print("\nPosts disponibles:")
            listar_posts(blog.listar_posts())

        elif opcion == 2:
            termino = pedir_texto("Buscar por título: ")
            if not termino:
                print("Ingresá un término para realizar la búsqueda.")
            else:
                print(f"\nResultados para '{termino}':")
                encontrados = blog.buscar_por_titulo(termino)
                listar_posts(encontrados)

        elif opcion == 3:
            tag = pedir_texto("Ingresá el tag a filtrar: ")
            if not tag:
                print("Ingresá un tag para realizar el filtrado.")
            else:
                print(f"\nPosts con el tag '{tag}':")
                encontrados = blog.filtrar_por_tag(tag)
                listar_posts(encontrados)

        elif opcion == 4:
            datos = pedir_datos_post()
            autor = Autor(datos["nombre_autor"], datos["bio_autor"])
            nuevo_post = Post(
                blog.siguiente_id(),
                datos["titulo"],
                datos["contenido"],
                autor,
                datos["tags"],
                datos["estado"],
                datos["categoria"],
            )

            es_valido, mensaje = validar_post(nuevo_post)
            if not es_valido:
                print(f"No se creó el post: {mensaje}")
            else:
                blog.agregar_post(nuevo_post)
                print("Post creado correctamente.")
                if guardar_posts(blog.posts):
                    print("Los cambios también se guardaron en posts.json.")
                else:
                    print("El post quedó en memoria, pero no se pudo guardar en JSON.")

        elif opcion == 5:
            validar_todos_los_posts(blog.posts)

        elif opcion == 6:
            if guardar_posts(blog.posts):
                print("Posts guardados correctamente en posts.json.")

        elif opcion == 7:
            print("\nGracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida, intentá de nuevo.")


if __name__ == "__main__":
    main()
