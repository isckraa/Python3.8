a = [1,1,1,3,1,4,1,1,3,6,1,2,3,1,4]

print(a)
print("Nombre de 3 :", a.count(3))
a.reverse()
print("Dernier 3 Ã  la position", len(a)-a.index(3))

a.remove(3)
a.reverse()

print(a)
print("Nombre de 3 :", a.count(3))
a.reverse()
print("Dernier 3 a la position", len(a)-a.index(3))