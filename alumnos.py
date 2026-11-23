def agregar_alumno(alumnos, dni, nombre, apellido, curso, nota):
    """Crea un registro (diccionario) y lo agrega a la lista de alumnos."""
    if buscar_alumno(alumnos, dni) is not None:
        print("Ya existe un alumno registrado con ese DNI.")
        return

    alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "curso": curso,
        "nota": nota
    }
    alumnos.append(alumno)
    print("Alumno agregado correctamente.")


def listar_alumnos(alumnos):
    """Muestra todos los registros almacenados."""
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    print("\n--------- LISTA DE ALUMNOS ---------")
    for alumno in alumnos:
        print(
            f"DNI: {alumno['dni']} | "
            f"Nombre: {alumno['nombre']} {alumno['apellido']} | "
            f"Curso: {alumno['curso']} | Nota: {alumno['nota']}"
        )


def buscar_alumno(alumnos, dni):
    """Busca un alumno por DNI y devuelve su diccionario o None."""
    for alumno in alumnos:
        if alumno["dni"] == dni:
            return alumno
    return None


def modificar_nota(alumnos, dni, nueva_nota):
    """Actualiza la nota del alumno identificado por DNI."""
    alumno = buscar_alumno(alumnos, dni)
    if alumno is None:
        print("No se encontró un alumno con ese DNI.")
        return

    alumno["nota"] = nueva_nota
    print("Nota modificada correctamente.")


def eliminar_alumno(alumnos, dni):
    """Elimina de la lista el alumno identificado por DNI."""
    alumno = buscar_alumno(alumnos, dni)
    if alumno is None:
        print("No se encontró un alumno con ese DNI.")
        return

    alumnos.remove(alumno)
    print("Alumno eliminado correctamente.")


def calcular_promedio(alumnos):
    """Calcula el promedio de las notas. Devuelve None si no hay alumnos."""
    if not alumnos:
        return None

    suma = 0
    for alumno in alumnos:
        suma += alumno["nota"]

    return suma / len(alumnos)


def mostrar_mejor_nota(alumnos):
    """Muestra el alumno o los alumnos que tienen la nota más alta."""
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    mejor_nota = max(alumno["nota"] for alumno in alumnos)
    print(f"Mejor nota: {mejor_nota}")

    for alumno in alumnos:
        if alumno["nota"] == mejor_nota:
            print(f"{alumno['nombre']} {alumno['apellido']} - DNI: {alumno['dni']}")


def mostrar_aprobados_desaprobados(alumnos):
    """Muestra aprobados y desaprobados. Se considera aprobado desde 6."""
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    print("\nALUMNOS APROBADOS (nota igual o mayor a 6):")
    hay_aprobados = False
    for alumno in alumnos:
        if alumno["nota"] >= 6:
            print(f"{alumno['nombre']} {alumno['apellido']} - Nota: {alumno['nota']}")
            hay_aprobados = True
    if not hay_aprobados:
        print("No hay alumnos aprobados.")

    print("\nALUMNOS DESAPROBADOS (nota menor a 6):")
    hay_desaprobados = False
    for alumno in alumnos:
        if alumno["nota"] < 6:
            print(f"{alumno['nombre']} {alumno['apellido']} - Nota: {alumno['nota']}")
            hay_desaprobados = True
    if not hay_desaprobados:
        print("No hay alumnos desaprobados.")
