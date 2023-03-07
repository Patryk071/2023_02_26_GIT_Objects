#Import z pliku

listaOsob = []

with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    #cala_tresc = file.read()
    for line in file:
        listaOsob.append(tuple(line.replace("\n", "").split()))

print(listaOsob)
print(listaOsob[0])     ##osoba na miejscu 0
print(listaOsob[0][0])  #imię osoby na miejscu 0

# Zapisanie imion z list osób do pliku "imiona.txt"
with open("imiona.txt", "w", encoding="UTF-8") as file:
    for item in listaOsob:
        file.write(item[0] + "\n")

# Zapisanie nazwisk z list osób do pliku "nazwiska.txt"
with open("nazwiska.txt", "w", encoding="UTF-8") as file:
    for item in listaOsob:
        # ZAPIS warunku z IF
        #if len(item) == 2: ##ten warunek jest niezbędny w przypadku,
        #                    ## gdy w tupli brak nazwiska
        #    file.write(item[1] + "\n")
        #else:
        #    file.write("\n")

        # ZAPIS warunku z try (obsługa wyjątków)
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")