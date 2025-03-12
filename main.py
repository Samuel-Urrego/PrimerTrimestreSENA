"""Creación de variables básicas"""

nombre = "Luis"
apellido = "Maturana"
nombre_completo= nombre + " " + apellido
edad = 30
estatura = 1.80
peso = 96
docente = True

salario_enero = 1000
salario_febrero = 1100
salario_marzo =800
salario_trimestre = salario_enero + salario_febrero + salario_marzo

print(nombre_completo, edad, "años")
print(nombre_completo,  "me gane los 2 primeros meses", salario_enero + salario_febrero)
print(nombre_completo,  "me gane los 3 primeros meses", salario_trimestre)