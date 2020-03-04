import math

class Nombre:
    def __init__(self, imaginaire = 0, reelle = 0):
        self.__pImaginaire = imaginaire
        self.__pReelle = reelle
    
    def getPImaginaire(self):
        return self.__pImaginaire
    def getPReelle(self):
        return self.__pReelle
    
    def setPImaginaire(self, imaginaire):
        self.__pImaginaire = imaginaire
    def setPReelle(self, reelle):
        self.__pReelle = reelle

    def additionne(self, nombre):
        nb = Nombre()
        nb.setPImaginaire(self.getPImaginaire() + nombre.getPImaginaire())
        nb.setPReelle(self.getPReelle() + nombre.getPReelle())
        return nb
    
    def affiche(self):
        print(self.getPReelle(),"+ix",self.getPImaginaire())

class Reel(Nombre):
    def __init__(self, imaginaire = 0, reelle = 0):
        Nombre.__init__(self)
        self.__pImaginaire = 0
        self.__pReelle = reelle
    
    def getPReelle(self):
        return self.__pReelle

    def ent(self):
        return math.floor(self.getPReelle())

# Nombre
print("**Nombre**")
nb1 = Nombre(1,2)
nb1.affiche()

nb2 = Nombre(-5,8)
nb2.affiche()

nb1.additionne(nb2).affiche()

# Reel
print("\n**Reel**")
r1 = Reel(5,8.9)
print(r1.getPImaginaire())
print(r1.ent())
