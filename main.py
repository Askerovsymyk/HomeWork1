class SuperHero:
    def __init__(self, name, hp, power, people='human'):
        self.name = name
        self.hp = hp
        self.power = power
        self.people = people

    def multiply_hp(self):
        self.hp *= 2

class AirHero(SuperHero):
    def __init__(self, name, hp, power, damage, people='human'):
        super().__init__(name, hp, power, people)
        self.damage = damage
        self.fly = False

    def multiply_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

class EarthHero(SuperHero):
    def __init__(self, name, hp, power, damage, people='human'):
        super().__init__(name, hp, power, people)
        self.damage = damage
        self.fly = False

    def multiply_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

class SpaceHero(SuperHero):
    def __init__(self, name, hp, power, damage, people='human'):
        super().__init__(name, hp, power, people)
        self.damage = damage
        self.fly = False

    def multiply_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

air_hero = AirHero('Airman', 100, 50, 30)
earth_hero = EarthHero('Earthman', 120, 40, 25)
space_hero = SpaceHero('Spaceman', 150, 60, 35)

air_hero.multiply_hp()
print(f"{air_hero.name} HP: {air_hero.hp}, Fly: {air_hero.fly}")
air_hero.true_phrase()

earth_hero.multiply_hp()
print(f"{earth_hero.name} HP: {earth_hero.hp}, Fly: {earth_hero.fly}")
earth_hero.true_phrase()

space_hero.multiply_hp()
print(f"{space_hero.name} HP: {space_hero.hp}, Fly: {space_hero.fly}")
space_hero.true_phrase()

class Villain(AirHero):
    def __init__(self, name, hp, power, damage):
        super().__init__(name, hp, power, damage)
        self.people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2

villain = Villain('BadGuy', 200, 70, 40)

print(f"Before crit: {villain.name} Damage: {villain.damage}")
villain.crit()
print(f"After crit: {villain.name} Damage: {villain.damage}")

air_hero.damage = 20
print(f"AirHero Before crit: {air_hero.damage}")
villain.crit()
print(f"AirHero After crit: {air_hero.damage}")
