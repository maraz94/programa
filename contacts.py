from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def show_menu():
    print("Acciones disponibles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")

    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action)not in MENU_OPTIONS):
        selected_action = input("¿Qué opción deseas?")
    return int(selected_action)


def add_contact(contacts):
    print("\n\nañadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "Phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente".format(contact["name"]))
    sleep(2)

def remove_contact(contacts):
    print("\n\nbuscar contacto\n")
    search_item = input("Introduce el nombre o parte de él: ")


def find_contact(contacts):
    pass


def export_contact():
    pass


def main():
    contacts = []
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contact()




        action = show_menu()

    #Exit the program








if __name__ == "__main__":
    main()