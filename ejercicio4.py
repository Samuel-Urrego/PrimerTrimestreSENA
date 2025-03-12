"""
Elabore un programa en Python que realice las operaciones de una calculadora, de forma que le pida al usuario 2 números, 
y con ellos imprima el resultado de la suma, resta, multiplicación, división y potencia de los números ingresados. 
Almacene el resultado de cada operación en variables individuales (No realice las operaciones directamente en el print() )

"""

num1 = int(input("Ingresa un numero entero"))
num2 = int(input("Ingresa un numero entero"))

suma = (num1 + num2)
resta = (num1 - num2)
multiplicacion = (num1 * num2)
division = (num1 / num2)
potencia = (num1 ** num2)

print("El resultado de la suma es:", " ", suma)
print("El resultado de la resta es:", " ", resta)
print("El resultado de la multiplicacion es:", " ", multiplicacion)
print("El resultado de la division es:", " ", division)
print("El resultado de la potencia4 es:", " ", potencia)