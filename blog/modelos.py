"""Clases que representan al autor, al post y al blog."""


class Autor:
    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales,
        }


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado, categoria=""):
        if not isinstance(autor, Autor):
            raise TypeError("El autor del post debe ser un objeto Autor.")

        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado
        self.categoria = categoria

    def a_diccionario(self):
        datos = {"id": self.id, "titulo": self.titulo}

        # El post 6 de la entrega anterior no tiene contenido a propósito.
        # Si es None, conservamos esa ausencia al guardar nuevamente el JSON.
        if self.contenido is not None:
            datos["contenido"] = self.contenido

        datos["autor"] = self.autor.a_diccionario()
        datos["categoria"] = self.categoria
        datos["tags"] = self.tags
        datos["estado"] = self.estado
        return datos


class Blog:
    def __init__(self, posts=None):
        self.posts = list(posts) if posts is not None else []

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, termino):
        resultados = []
        termino = termino.strip().lower()
        if not termino:
            return resultados

        for post in self.posts:
            if isinstance(post.titulo, str) and termino in post.titulo.lower():
                resultados.append(post)
        return resultados

    def filtrar_por_tag(self, tag):
        resultados = []
        tag = tag.strip().lower()
        if not tag:
            return resultados

        for post in self.posts:
            if isinstance(post.tags, list):
                for etiqueta in post.tags:
                    if isinstance(etiqueta, str) and etiqueta.lower() == tag:
                        resultados.append(post)
                        break
        return resultados

    def siguiente_id(self):
        mayor_id = 0
        for post in self.posts:
            if isinstance(post.id, int) and not isinstance(post.id, bool):
                if post.id > mayor_id:
                    mayor_id = post.id
        return mayor_id + 1

    def agregar_post(self, post):
        if not isinstance(post, Post):
            raise TypeError("Solo se pueden agregar objetos Post al blog.")
        self.posts.append(post)
