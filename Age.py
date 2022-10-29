"""
paralelo: 
Escribir un programa que pregunte al usuario su edad
y muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad).
"""

age = int(input("Ingrese su edad a continuacion: "))
edadArray = []

for i in range(1,age+1):
    edadArray.append(str(i))

edadString = " ".join(edadArray)
print("Usted ha cumplido los siguiente años:",edadString)