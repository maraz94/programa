class BasePokemon:
    base_health_point = 100
    damage = 10
    name = "Pokemon"
    attacks = []

    def __init__(self):
        self.health_point = self.base_health_point

    def fight(self, enemy, attack_name=None):
        if not attack_name:
            enemy.take_damage(self.damage)
        else:
            for attack in self.attacks:
                if attack.name == attack_name:
                    enemy.take_damage(attack.ataque)
                    return

    def take_damage(self, damage):
        self.health_point -= damage

    def show_health_points(self):
        print("Vida actual de {}".format(self.name, self.health_point))


class BasePokemonAttack:
    name = ""
    damage = 0


class ChispazoAttack(BasePokemon):
    name = "Chispazo"
    damage = 10

class BolaVoltioAttack(BasePokemon):
    name = "Bola Voltio"
    damage = 9


class Charmander(BasePokemon):
    base_health_point = 100
    damage = 10
    name = "Charmander"


class Pikachu(BasePokemon):
    base_health_point = 120
    damage = 12
    name = "Pikachu"
    attacks = [ChispazoAttack, BolaVoltioAttack]


class Bulbasur(BasePokemon):
    base_health_point = 90
    damage = 7
    name = "Bulbasur"


class Squirtle(BasePokemon):
    base_health_point = 100
    damage = 3
    name = "Squirtle"


