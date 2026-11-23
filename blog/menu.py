"""Menú y entradas de datos del usuario por consola."""


def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    try:
        return int(input("Seleccioná una opción (1-7): "))
    except ValueError:
        print("Error: debés ingresar un número del 1 al 7.")
        return 0


def pedir_texto(mensaje):
    return input(mensaje).strip()


def pedir_datos_post():
    print("\n--- CREAR NUEVO POST ---")
    titulo = pedir_texto("Título: ")
    contenido = pedir_texto("Contenido: ")
    nombre_autor = pedir_texto("Nombre del autor: ")
    bio_autor = pedir_texto("Biografía del autor (opcional): ")
    categoria = pedir_texto("Categoría (opcional): ")
    texto_tags = pedir_texto("Etiquetas separadas por coma: ")
    estado = pedir_texto("Estado (borrador, publicado, archivado): ").lower()

    tags = []
    for etiqueta in texto_tags.split(","):
        etiqueta = etiqueta.strip()
        if etiqueta:
            tags.append(etiqueta)

    return {
        "titulo": titulo,
        "contenido": contenido,
        "nombre_autor": nombre_autor,
        "bio_autor": bio_autor,
        "categoria": categoria,
        "tags": tags,
        "estado": estado,
    }
