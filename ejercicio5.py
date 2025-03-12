#Dolares y pesos colombianos

bolsilloIzq = int(input("Digita los dolares que tienes"))
bolsilloDer = int(input("Digita los pesos colombianos que tienes"))

dvd = int(input("Digita el precio del DVD"))
pasaje = int(input("Digita el precio del pasaje"))
reciboDeLuz = int(input("Digita el precio del recibo de luz"))
libro = int(input("Digita el precio del libro"))
pagoDolares = int(input("Digita el pago que te hicieron en dolares"))
almuerzo = int(input("Digita el precio del almuerzo"))
pagocop = int(input("Digita el pago que te hicieron en pesos colombianos"))
cine = int(input("Digita el precio de las entradas de cine"))    

totalUSD = bolsilloIzq - dvd - libro + pagoDolares
totalCOP = bolsilloDer - pasaje - reciboDeLuz - almuerzo - cine + pagocop

print("Tienes", totalCOP, "pesos colombianos en el bolsillo derecho")
print("Tienes" ,totalUSD,"dolares en el bolsillo izquierdo")