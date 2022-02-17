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



cursor = conexion.cursor()
ope = str(input("ingrese la operacion: "))
num1 = int(input("Ingrese el sumando: "))
num2 = int(input("Ingrese el sumando: "))
suma = num1+num2
SQL = "INSERT INTO DatosCalculadora(Operacion,  Numero_1,  Numero_2, Resultado) VALUES(%s, %s, %s, %s)" 
cursor.execute(SQL,(ope,num1, num2, suma))
conexion.commit()
cursor.close()
conexion.close()