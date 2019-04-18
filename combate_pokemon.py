#Pikachu = 100 vida; ataques: chispazo=10 daño; Bola voltio=12 daño
#Bulbasur = 100 vida; 10 daño
#Charmander= 80 vida; 7 daño
#Squirtle= 90 vida; 8 daño

pokemon_elegido = input("¿Quien será tu adversario? (Squirtle / Charmander / Bulbasur / Maquina de Combate): ").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "SQUIRTLE"
    ataque_pokemon = 8

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "CHARMANDER"
    ataque_pokemon = 7

elif pokemon_elegido == "BULBASUR":
    vida_enemigo = 100
    nombre_pokemon = "BULBASUR"
    ataque_pokemon = 10

elif pokemon_elegido == "MAQUINA DE COMBATE":
    vida_enemigo = 2000
    nombre_pokemon = "MAQUINA DE COMBATE"
    ataque_pokemon = 99

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque quieres usar? (Chispazo / Bola Voltio" ).upper()

    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    elif ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12

    print("La vida del {} ahora es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace {} puntos de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("La vida de tu Pikachu ahora es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")
if vida_pikachu <= 0:
    print("Has perdido")

print("El Combate ha terminado")
