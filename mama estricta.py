leche=input("¿Trajo la leche? \n Digite Si o No \n")
pan=input("¿Trajo el pan? \n Digite Si o No \n")
huevos=input("¿Trajo los huevos? \n Digite Si o No \n")

#Mama estricta
if leche=="si" and pan=="si" and huevos=="si":
    print("Era lo minimo venga y desayune")
else:
    print("Lo mata")
    
#Mama comprensiva

if leche=="si" or pan=="si" or huevos=="si":
    print("Que niño tan inteligente")
else:
    print("Venga yo voy")
