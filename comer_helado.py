
apetece_helado_input = input("Te hapetece un helado? (si / no) ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Eso es un No.")
    apetece_helado = False


tienes_dinero_input = input("Tienes dinero? (si / no) ").upper()
esta_senor_helado_input = input("Esta el señor de los helado? (si / no) ").upper()
esta_tu_tia_input = input("estas con tu tia? (si / no) ").upper()

apetece_helado = apetece_helado_input == "SI"
puedes_permitirlo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_senor_helado = esta_senor_helado_input == "SI"


if apetece_helado and puedes_permitirlo and esta_senor_helado:
    print("Pues comete un helado")
else:
    print("pues no hay helado")

