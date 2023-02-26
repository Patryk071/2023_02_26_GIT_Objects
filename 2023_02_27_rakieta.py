from random import randint

class Rocket:
    def __init__(self):
        self.altitude = 0

    def __str__(self):
        return "Hejka, jestem rakietą! I znajduje się na wysokości " + str(self.altitude)

    def move(self):
        self.altitude += 1


rakiety = []

for i in range(5):
    nowaRakieta = Rocket()
    rakiety.append(nowaRakieta)

for rakieta in rakiety:
    print(rakieta)

for i in range(100):
    indexDoPoruszania = randint(0, 4)
    rakiety[indexDoPoruszania].move()

for rakieta in rakiety:
    print("Moja aktualna wysokość to: ", rakieta.altitude)
