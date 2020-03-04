tab = list(range(100))
tabDiv = []

diviseur = int(input("Saisissez un nombre diviseur : "))

for index in range(len(tab)):
    if tab[index]%diviseur == 0:
        tabDiv.append(index)

print("Voici la liste des multiples de",diviseur,"inférieurs à 100 :",tabDiv)
