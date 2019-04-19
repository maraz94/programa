
salida = False
agenda = dict()

while not salida:
    accion = input("¿qué Quieres Hacer? [Añadir número[A] / Consultar Número [C] / Salir[S]")
    if accion == "A":
        print("Vamos a añadir un número de teléfono:")
        print("-------------------------------------")
        nombre =input("Nombre: ")
        numero= input("Número: ")
        agenda[nombre] = numero

    elif accion == "C":
        print("Vamos a consultar un número")
        print("-------------------------------------")
        nomnre = input("De quien quieres saber el número?")
        print(agenda[nombre])

    elif accion == "S":
        salida = True