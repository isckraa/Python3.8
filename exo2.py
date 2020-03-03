a = []

depart = int( input( "Saisissez un nombre de départ : " ) )
arrive = int( input( "Saisissez un nombre d'arrivé : " ) )
pas = int( input( "Saissisez un pas : " ) )

a.append( depart )
a.append( arrive )
a.append( pas )

a.extend( list( range( a[0], a[1], a[2] ) ) )
print( "Liste: ", a )

print( "Pas des derniers éléments de la liste : ", a[-1 * pas:] )
#print( "Pas des derniers éléments de la liste : ", a[-pas:] )
