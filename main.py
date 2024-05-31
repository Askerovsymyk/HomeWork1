class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_hero(self):
        print(f"Name of the hero: {self.name}")

    def double_health(self):
        self.health_points *= 2
        print(f"Health points after doubling: {self.health_points}")

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Syimyk", "Askerov", "programmist", 100, "not one step back")

hero.name_hero()
hero.double_health()
print(hero)
print(f"Length of catchphrase: {len(hero)}")

