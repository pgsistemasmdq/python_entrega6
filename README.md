# Preentrega 6: Blog con POO y persistencia JSON

Esta versión continúa el proyecto modular de la **Entrega 5**, conservando las publicaciones, títulos, etiquetas y autor de las entregas anteriores. Ahora el sistema trabaja con **objetos de Python** y permite **guardar y recuperar publicaciones mediante `posts.json`**.


## Cómo ejecutar

1. Abrí la carpeta `blog_consola` en Visual Studio Code.
2. Abrí **Terminal > Nueva terminal**.
3. Desde la carpeta que contiene `main.py`, ejecutá:

   ```powershell
   python main.py
   ```

   En Windows también podés usar `py main.py`.

No hay que ejecutar los archivos dentro de `blog/` por separado.

## Estructura

```text
blog_consola/
├── .gitignore
├── README.md
├── main.py
├── posts.json
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Qué hace cada archivo

- **`main.py`**: inicia el blog y coordina las opciones del menú.
- **`blog/modelos.py`**: define las clases `Autor`, `Post` y `Blog`.
- **`blog/datos.py`**: carga datos de `posts.json`, los convierte en objetos y guarda los posts como diccionarios JSON. Mantiene los estados y etiquetas del blog.
- **`blog/menu.py`**: pide datos al usuario y muestra el menú.
- **`blog/operaciones.py`**: muestra listas de objetos `Post` en pantalla.
- **`blog/validaciones.py`**: verifica los datos de los objetos `Post`.
- **`blog/__init__.py`**: identifica el paquete `blog`.
- **`posts.json`**: contiene las publicaciones entre ejecuciones.

## Las tres clases

- **`Autor`**: representa a una persona, con nombre, biografía y datos opcionales. Su método `a_diccionario()` permite guardar el autor en JSON.
- **`Post`**: tiene ID, título, contenido, categoría, etiquetas, estado y una instancia de `Autor` (no solo un nombre). Su método `a_diccionario()` transforma el post completo en tipos compatibles con JSON.
- **`Blog`**: administra una lista de objetos `Post` y ofrece métodos para listar, buscar por título, filtrar por tag, generar el siguiente ID y agregar posts.

## Cómo funciona la persistencia

1. Al iniciar, `cargar_posts()` abre `posts.json` con `json.load()`.
2. Cada diccionario del archivo se convierte en un `Autor` y un `Post`.
3. `main.py` crea un objeto `Blog` con esa lista de publicaciones.
4. Al crear un post válido se agrega al blog y **se guarda automáticamente** en `posts.json`.
5. También se puede guardar manualmente desde la opción 6 del menú.
6. Para guardar, `guardar_posts()` convierte cada `Post` a diccionario y usa `json.dump()`.
7. Al cerrar y volver a abrir el programa se recuperan los posts guardados.

Si falta `posts.json`, comienza con una lista vacía. Si está vacío o no contiene un JSON válido, muestra un mensaje claro sin cerrar el programa. El archivo incluido inicialmente contiene los **seis posts de la Entrega 5**, incluido el **post 6 sin contenido a propósito**, para probar el validador.

## Menú

1. Ver todos los posts.
2. Buscar por título (ignorando mayúsculas y minúsculas).
3. Filtrar por tag (ignorando mayúsculas y minúsculas).
4. Crear un nuevo post (solicita sus datos, valida y guarda en JSON).
5. Validar posts (informa errores, especialmente el post 6).
6. Guardar posts en JSON.
7. Salir.

## Prueba de persistencia

1. Ejecutá `python main.py`.
2. Elegí **4** y creá un post, con título, contenido, autor y estado válidos.
3. Comprobá que aparezca el mensaje de guardado.
4. Elegí **7** para cerrar el programa.
5. Ejecutá de nuevo `python main.py`.
6. Elegí **1** para listar y comprobá que tu nuevo post siga presente.
7. Probá **2** y **3** para buscarlo por título o etiqueta.

También podés probar la opción **5**: el post 6 original se informa como inválido porque no tiene contenido.
