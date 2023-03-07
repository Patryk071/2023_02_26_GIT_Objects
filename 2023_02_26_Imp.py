#Import z pliku

with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    #cala_tresc = file.read()
    for line in file:
        print(line.replace("\n", "").split())

#print(cala_tresc)

with open("imiona.txt", "w", encoding="UTF-8") as file:
    pass