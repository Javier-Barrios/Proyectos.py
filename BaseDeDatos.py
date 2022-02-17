#  Javier Andrés Barrios del Aguila 
#  201801376

import psycopg2

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "javier",
        password = "javier",
        dbname = "Calculadora"
    )
    print("conexion exitosa")
except psycopg2.Error as e:
    print("Error en la conexión \nverificar parametros \n")



def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, ingrese un número")  
    return numero
 
calcu = int(input("Operación a Realizar: \n \n 1- Suma \n 2- Resta \n 3- Multiplicación \n 4- División \n 5- Potencia \n 6- Raiz \n 7- Historial \n 0- Salir \n \n"))
while calcu != 0: 
    if calcu == 1:
        num1 = input_numero("Ingrese el sumando: ")
        num2 = input_numero("Ingrese el sumando: ")
        suma = num1+num2
        print("La suma es: ", suma, "\n")

        cursor = conexion.cursor()
        SQL = "INSERT INTO DatosCalculadora(Operacion,  Numero_1,  Numero_2, Resultado) VALUES('Suma', %s, %s, %s)" 
        cursor.execute(SQL,(num1, num2, suma))
        conexion.commit()
        cursor.close()
        conexion.close()
                
    elif calcu == 2:
        num1 = input_numero("Ingrese el minuendo: ")
        num2 = input_numero("Ingrese el sustraendo: ")
        resta = num1-num2
        print("La resta es: ", resta, "\n")

        cursor = conexion.cursor()
        SQL = "INSERT INTO DatosCalculadora(Operacion,  Numero_1,  Numero_2, Resultado) VALUES('Resta', %s, %s, %s)" 
        cursor.execute(SQL,(num1, num2, resta))
        conexion.commit()
        cursor.close()
        conexion.close()

    elif calcu == 3:
        num1 = input_numero("Ingrese el multiplicando: ")
        num2 = input_numero("Ingrese el multiplicador: ")
        mult = num1*num2
        print("La multiplicación es: ", mult, "\n")

        cursor = conexion.cursor()
        SQL = "INSERT INTO DatosCalculadora(Operacion,  Numero_1,  Numero_2, Resultado) VALUES('Multiplicación', %s, %s, %s)" 
        cursor.execute(SQL,(num1, num2, mult))
        conexion.commit()
        cursor.close()
        conexion.close()

    elif calcu == 4:
        try: 
            num1 = input_numero("Ingrese el dividendo: ")
            num2 = input_numero("Ingrese el divisor: ")
            div = num1/num2
            print("La división es: ", div, "\n")
        except ZeroDivisionError: 
            print("el segundo numero no puede ser 0")
        except:
            print("solo puede ingresar numeros")
        
        cursor = conexion.cursor()
        SQL = "INSERT INTO DatosCalculadora(Operacion,  Numero_1,  Numero_2, Resultado) VALUES('División', %s, %s, %s)" 
        cursor.execute(SQL,(num1, num2, div))
        conexion.commit()
        cursor.close()
        conexion.close()
        
    elif calcu == 5:
        num1 = input_numero("Ingrese la base de la potencia: ")
        num2 = input_numero("Ingrese el exponente de la potencia: ")
        pot = pow(num1, num2)
        print("La potencia es: ", pot, "\n")  

        cursor = conexion.cursor()
        SQL = "INSERT INTO DatosCalculadora(Operacion,  Numero_1,  Numero_2, Resultado) VALUES('Potencia', %s, %s, %s)" 
        cursor.execute(SQL,(num1, num2, pot))
        conexion.commit()
        cursor.close()
        conexion.close()

    elif calcu == 6:        
        num1 = input_numero("Ingrese el radicando de la raiz: ")
        num2 = input_numero("Ingrese el indice de la raiz: ")
        raiz = pow(num1, (1/num2))
        print("La raiz es: ", raiz, "\n") 

        cursor = conexion.cursor()
        SQL = "INSERT INTO DatosCalculadora(Operacion,  Numero_1,  Numero_2, Resultado) VALUES('Raiz', %s, %s, %s)" 
        cursor.execute(SQL,(num1, num2, raiz))
        conexion.commit()
        cursor.close()
        conexion.close()
    
    elif calcu == 7:
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM DatosCalculadora;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()

    else :
        print("Escriba una opcion correcta")
    calcu = int(input("Operación a Realizar: \n \n 1- Suma \n 2- Resta \n 3- Multiplicación \n 4- División \n 5- Potencia \n 6- Raiz \n 7- Historial \n 0- Salir \n \n "))
