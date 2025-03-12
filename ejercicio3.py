"""Tres hermanos, Hugo, Paco y Luis, deciden hacer “vaca” para comprar un Play Station 5 que vale $ 3.200.000 .
Si la consola es comprada antes de marzo, el almacén les concederá un 8% de descuento. Los hermanos saben que
Tío Rico les dará como obsequio el 20% del valor de la consola Hugo como hermano mayor, aportará sus ahorros y 
cubrirá el 50% del valor de la Play 5. Paco dice que aportará al 17 % del valor de la consola.
Elabore un programa en Python e imprima las respuestas para:
¿Cuánto dinero """


valor_consola = 3200000
descuento_marzo = 0.08
tio = 0.20
hugo = 0.50 
paco = 0.17
luis = 1 - (tio+hugo+paco)

valor_consola_febrero = (valor_consola -(valor_consola * descuento_marzo))
valor_tio = (valor_consola_febrero * tio)
valor_hugo = (valor_consola_febrero * hugo)
valor_paco = (valor_consola_febrero * paco)
valor_luis = (valor_consola_febrero * luis)

valor_tio2 = (valor_consola * tio)
valor_hugo2 = (valor_consola * hugo)
valor_paco2 = (valor_consola * paco)
valor_luis2 = (valor_consola * luis)


valor_equitativo = ((valor_consola_febrero - 1500000)/3)

print("Valor de la consola en febrero "," ", valor_consola_febrero)
print("El tio va a dar:"," ", valor_tio)
print("Hugo va a dar:"," ", valor_hugo)
print("Paco va a dar:"," ", valor_paco)
print("Luis va a dar:"," ", valor_luis)
print("El valor de la consola en marzo es:", " ", valor_consola)
print("Tio en marzo va a dar:", " ", valor_tio2)
print("Hugo en marzo va a dar:", " ", valor_hugo2)
print("Paco en marzo va a dar:", " ", valor_paco2)
print("Luis en marzo va a dar:", " ", valor_luis2)
print("Si el Tio pone 1'500.000 a los hermanos les tocaría poner:", " ", valor_equitativo)