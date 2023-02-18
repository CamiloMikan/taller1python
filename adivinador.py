print("piensa un numero")
print("ahora sumale 5")
print ("A este numero multiplicalo por 3")
print (" y por ultimo restale 15")

numero=int(input("Ingrese el resultado obtenido \n"))
operacion= numero/3

print("el resultado es ", operacion,)

resultado=input("¿es correcto el resultado? Si o No \n")

if resultado=="Si" or "si" or "SI":
    print("Soy todo un adivino")
else:
    print("rectifica tu respuesta")
