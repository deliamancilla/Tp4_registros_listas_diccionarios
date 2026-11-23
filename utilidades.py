def ingresar_texto(mensaje):
    """Solicita un texto y evita que se ingrese vacío."""
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("Este campo no puede quedar vacío.")


def ingresar_nota(mensaje):
    """Solicita una nota numérica entre 0 y 10."""
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 10:
                return nota
            print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Ingrese un número válido.")
