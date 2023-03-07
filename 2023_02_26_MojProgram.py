#Classy do programu "Mój program" są w innym pliku "rakieta"

from rakieta import RocketBoard

plansza = RocketBoard()


## Tutaj odwołujemy się do "planszy.rekiety[3]", bo inaczej system
## nie będzie wiedział który element z RocketBoard nam pokazać
#print("Wysokość 3 elementu: ", plansza.rakiety[2].altitude)

# Po dodaniu w RocketBoard "def __getitem__(self, item):"
# classa RocketBoard będzie zwracać to co wskażemy w return
# w tym przypadku "rakiety[x]"

print("")
print(plansza[1])
print("Wysokość 3 elementu: ", plansza[2].altitude)
print(plansza[1] + plansza[2])