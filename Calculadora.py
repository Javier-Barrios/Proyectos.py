def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, ingrese un número")
    return numero
 
calcu = int(input("Operación a Realizar: \n 1- Suma \n 2- Resta \n 3- Multiplicación \n 4- División \n 5- Potencia \n 6- Raiz \n 0- Salir \n"))
while calcu != 0: 
    if calcu == 1:
        num1 = input_numero("Ingrese el sumando: ")
        num2 = input_numero("Ingrese el sumando: ")
        suma = num1+num2
        print("La suma es: ", suma, "\n")
    elif calcu == 2:
        num1 = input_numero("Ingrese el minuendo: ")
        num2 = input_numero("Ingrese el sustraendo: ")
        resta = num1-num2
        print("La resta es: ", resta, "\n")
    elif calcu == 3:
        num1 = input_numero("Ingrese el multiplicando: ")
        num2 = input_numero("Ingrese el multiplicador: ")
        mult = num1*num2
        print("La multiplicación es: ", mult, "\n")
    elif calcu == 4:
        num1 = input_numero("Ingrese el dividendo: ")
        num2 = input_numero("Ingrese el divisor: ")
        div = num1/num2
        print("La división es: ", div, "\n")
    elif calcu == 5:
        num1 = input_numero("Ingrese la base de la potencia: ")
        num2 = input_numero("Ingrese el exponente de la potencia: ")
        pot = pow(num1, num2)
        print("La potencia es: ", pot, "\n")    
    elif calcu == 6:        
        num1 = input_numero("Ingrese el radicando de la raiz: ")
        num2 = input_numero("Ingrese el indice de la raiz: ")
        raiz = pow(num1, (1/num2))
        print("La raiz es: ", raiz, "\n") 
    else :
        print("Escriba una opcion correcta")
    calcu = int(input("Operación a Realizar: \n 1- Suma \n 2- Resta \n 3- Multiplicación \n 4- División \n 5- Potencia \n 6- Raiz \n 0- Salir \n"))