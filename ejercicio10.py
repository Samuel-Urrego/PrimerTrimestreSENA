#Cuenta de ahorros

dineroDepositado = int(input("Digite la cantidad de dinero depositado"))
interes1 = dineroDepositado * 1.04
interes2 = interes1 * 1.04
interes3 = interes2 * 1.04

interes1Redondeado = round(interes1, 2)
interes2Redondeado = round(interes2, 2)
interes3Redondeado = round(interes3, 2)

print("El interes del primer año es: ", interes1Redondeado)
print("El interes del segundo año es: ", interes2Redondeado)
print("El interes del tercer año es: ", interes3Redondeado)



