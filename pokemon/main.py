from pokemon import Squirtle, Charmander, Bulbasur, Pikachu
"""


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
"""
def choose_pokemon():
    choosen_pokemon = input("¿Quien será tu adversario? (Squirtle / Charmander / Bulbasur / : ").upper()

    if choosen_pokemon == "SQUIRTLE":
        return Squirtle()
    elif choosen_pokemon == "CHARMANDER":
        return Charmander()
    elif choosen_pokemon == "BULBASUR":
        return Bulbasur()
def main():
    enemy = choose_pokemon()
    pikachu = Pikachu()

    while enemy.vida > 0 and pikachu.vida > 0:
        ataque_elegido = input("¿Que ataque quieres usar? (Chispazo / Bola Voltio").upper()
        if ataque_elegido == "CHISPAZO":
            vida_enemigo -= 10
        elif ataque_elegido == "BOLA VOLTIO":
            vida_enemigo -= 12

if __name__ == "__main__":
    main()
