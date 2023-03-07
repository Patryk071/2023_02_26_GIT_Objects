#Classy do programu "Mój program" są w innym pliku "rakieta"

from rakieta import RocketBoard

plansza = RocketBoard()

print("Wysokość 3 elementu: ", plansza.rakiety[2].altitude)
print(plansza[1])

print("Wysokość 3 elementu: ", plansza[2].altitude)

print(plansza[1] + plansza[2])