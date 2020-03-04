liste = list(range(3,16))
listeTemp = liste[:]
existe = True

print(liste)

while existe:
    number = int(input("Saisissez un nombre à supprimmer dans la liste : "))

    if number in listeTemp:
        del(listeTemp[listeTemp.index(number)])
        print(listeTemp)
    else:
        print(number,"n'est pas présent dans la liste")
        print("Liste initiale :",liste)
        print("Liste finale :",listeTemp)
        existe = False