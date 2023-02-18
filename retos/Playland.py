edad=int(input("ingrese su edad \n "))

if 0<= edad <=4 :
    print("Puede entar gratis")
    
elif 4< edad <18:
    print("El cliente debe pagar 20.000 ")
    
elif 18< edad <=60:
    print("El cliente debe pagar 15.000 ")

elif edad >60:
    print("El cliente debe pagar 3.000 ")
    
else:
    print("El dato ingresado es incorrecto")