a = [1,1,1,3,1,4,1,1,3,6,1,2,3,1,4]
print("a =", a)

number = int(input("Saisissez un nombre que vous voullez cherchez dans la liste : "))

if number in a:
    print("Le nombre",number,"est présent",a.count(number),"fois dans la liste 'a'.")
else :
    print("Le nombre",number,"n'est pas présent dans la liste 'a'.")

b = a[:]
b.reverse()

position = len(a)-(b.index(number)+1)
print("Position du dernier",number,"dans la liste 'a' : ",position)

print("Suppréssion du dernier",number,"dans la liste 'a'.")
del(a[position])

print("a =",a)
print("Le nombre",number,"est présent",a.count(number),"fois dans la liste 'a'.")

b = a[:]
b.reverse()

position = len(a)-(b.index(number)+1)
print("Position du dernier",number,"dans la liste 'a' : ",position)