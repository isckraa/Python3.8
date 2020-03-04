liste = [1]

iteration = int(input("Veuillez entrer le nombre d'itérations : "))

for i in range(iteration):
	listeTemp = []
	print(liste)
	for j in range(iteration**2):
		if j in liste:
			listeTemp.append(liste.count(j))
			listeTemp.append(j)
	liste.extend(listeTemp)
print(liste)