import random

moneda = random.randint(1, 2)

eleccion=int(input("escoja 1=cara 2=sello "))

if moneda==1:
    print("Salio Cara")
    
else:
    print("Salio sello")
    
if eleccion==moneda:
    print("ganaste")
else:
    print ("perdiste")
    