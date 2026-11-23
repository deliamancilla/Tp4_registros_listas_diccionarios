from alumnos import (
    agregar_alumno,
    listar_alumnos,
    buscar_alumno,
    modificar_nota,
    eliminar_alumno,
    calcular_promedio,
    mostrar_mejor_nota,
    mostrar_aprobados_desaprobados,
)
from utilidades import ingresar_texto, ingresar_nota


alumnos = []


def mostrar_menu():
    print("\n========== SISTEMA DE ALUMNOS ==========")
    print("1. Cargar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno por DNI")
    print("4. Modificar nota")
    print("5. Eliminar alumno")
    print("6. Calcular promedio general")
    print("7. Mostrar mejor nota")
    print("8. Mostrar aprobados y desaprobados")
    print("9. Salir")
    print("========================================")


def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            dni = ingresar_texto("Ingrese DNI: ")
            nombre = ingresar_texto("Ingrese nombre: ")
            apellido = ingresar_texto("Ingrese apellido: ")
            curso = ingresar_texto("Ingrese curso: ")
            nota = ingresar_nota("Ingrese nota (0 a 10): ")
            agregar_alumno(alumnos, dni, nombre, apellido, curso, nota)

        elif opcion == "2":
            listar_alumnos(alumnos)

        elif opcion == "3":
            dni = ingresar_texto("Ingrese el DNI que desea buscar: ")
            alumno = buscar_alumno(alumnos, dni)
            if alumno:
                print("\nAlumno encontrado:")
                print(f"DNI: {alumno['dni']}")
                print(f"Nombre: {alumno['nombre']} {alumno['apellido']}")
                print(f"Curso: {alumno['curso']}")
                print(f"Nota: {alumno['nota']}")
            else:
                print("No se encontró un alumno con ese DNI.")

        elif opcion == "4":
            dni = ingresar_texto("Ingrese el DNI del alumno: ")
            nueva_nota = ingresar_nota("Ingrese la nueva nota (0 a 10): ")
            modificar_nota(alumnos, dni, nueva_nota)

        elif opcion == "5":
            dni = ingresar_texto("Ingrese el DNI del alumno que desea eliminar: ")
            eliminar_alumno(alumnos, dni)

        elif opcion == "6":
            promedio = calcular_promedio(alumnos)
            if promedio is None:
                print("No hay alumnos registrados para calcular el promedio.")
            else:
                print(f"Promedio general: {promedio:.2f}")

        elif opcion == "7":
            mostrar_mejor_nota(alumnos)

        elif opcion == "8":
            mostrar_aprobados_desaprobados(alumnos)

        elif opcion == "9":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar()
