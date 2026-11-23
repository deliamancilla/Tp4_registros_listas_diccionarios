# TP N.º 4 – Registros, Listas y Diccionarios en Python

**Instituto de Educación Superior N.º 11**  
**Tecnicatura Superior en Desarrollo de Software**  
**Cátedra:** Programación 3  
**Docente:** Castro Abraham

## Sistema de alumnos en memoria

Este proyecto permite administrar alumnos mediante una lista de diccionarios en Python. Los datos se guardan en memoria mientras el programa está en ejecución; no utiliza una base de datos.

## Estructura del proyecto

```text
Tp4_registros_listas_diccionarios/
├── main.py
├── alumnos.py
├── utilidades.py
└── README.md
```

## Datos de cada alumno

Cada alumno se representa mediante un diccionario con las siguientes claves:

- `dni`
- `nombre`
- `apellido`
- `curso`
- `nota`

La lista `alumnos` contiene los registros de todos los estudiantes.

## Funcionalidades

1. Cargar alumnos.
2. Listar alumnos.
3. Buscar alumno por DNI.
4. Modificar la nota.
5. Eliminar alumno.
6. Calcular el promedio general.
7. Mostrar la mejor nota.
8. Mostrar estudiantes aprobados y desaprobados.
9. Salir del sistema.

Para este ejercicio se considera aprobado al alumno que obtiene una nota igual o superior a 6. Este criterio se utiliza como referencia en el programa.

## Requisitos

- Python 3.
- Visual Studio Code.
- Git.
- Cuenta de GitHub.

## Cómo ejecutar el programa

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir la terminal integrada.
3. Ejecutar:

```bash
python main.py
```

Si el comando anterior no funciona en Windows, probar:

```bash
py main.py
```

## Uso de Git y GitHub

Desde la terminal, dentro de la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Inicio TP4 listas y diccionarios"
git branch tp4
git checkout tp4
git add .
git commit -m "Sistema de alumnos en memoria"
```

Para publicar el proyecto, crear primero un repositorio vacío en GitHub y luego vincularlo:

```bash
git remote add origin URL_DEL_REPOSITORIO
git push -u origin tp4
```

Reemplazar `URL_DEL_REPOSITORIO` por la dirección real del repositorio creado en GitHub.

## Importante

Los registros se almacenan en memoria. Al cerrar el programa, los datos cargados se pierden, porque el trabajo solicita un sistema sin base de datos ni almacenamiento permanente.
