from random import randint


class Rocket:
    def __init__(self, predkosc = 1):
        self.altitude = 0
        self.speed = predkosc

    def __str__(self):
        return "Hejka, jestem rakietą! I znajduje się na wysokości " + str(self.altitude)

    def move(self):
        self.altitude += self.speed

    def __add__(self, other):
        return (self.speed + other.speed)


class RocketBoard:
    def __init__(self, liczbaRakiet = 5):
        self.rakiety = [Rocket() for _ in range(liczbaRakiet)]

        for _ in range(100):
            indexDoPoruszenia = randint(0, len(self.rakiety) - 1)
            self.rakiety[indexDoPoruszenia].move()

        for rakieta in self.rakiety:
            print(rakieta)

    def __getitem__(self, item):
        return self.rakiety


rakiety = []

#for rakieta in rakiety:
#    rakieta.speed = randint(1, 20)
#    print(rakieta, "i mam prędkość taką: ", rakieta.speed)
#
#for i in range(100):
#    indexDoPoruszania = randint(0, 4)
#    rakiety[indexDoPoruszenia].move()
#
#for rakieta in rakiety:
#    print("Moja aktualna wysokość to: ", rakieta.altitude)
