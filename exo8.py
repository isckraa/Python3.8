def getNbJours(annee=2016, mois=2) :
    listeJours = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if int(annee)%4 == 0:
        listeJours[1] = 29
    else:
        listeJours[1] = 28
    
    print("Année :",annee,", mois :",mois," nombre de jours :", listeJours[mois-1])

getNbJours()
getNbJours(2015)
getNbJours(2019,12)