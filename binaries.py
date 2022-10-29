# Nahuel Montes de Oca - AWS re/Start

# Escribir una funcion que convierta un 
# numero natural en binario y 
# otra que convierta un numero binario en decimal

def decimalToBinarie(num):
    # Para obtener el binario vamos a dividir por 2 cuantas veces sean necesarias
    respuesta = []
    while (num > 1): # Nuestra condicion de salida es llegar a 1
        resto = num%2 
        respuesta.insert(0,resto) # Agrego el resto de num/2 al final del array
        num = num//2 # Ahora num pasa a ser el cociente de num/2
    if (num==1): # Si ultimo cociente fue 1 lo agregamos al principio
        respuesta.insert(0,1)
    # Paso el array de respuesta a un string
    respuesta = ' '.join([str(elem) for elem in respuesta])
    return respuesta

# print("El 512 en binario es", decimalToBinarie(512))
# Fuente: 
# https://www3.gobiernodecanarias.org/medusa/ecoblog/juramgon/files/2017/09/conversion-de-decimal-a-binario-incluyendo-decimales.pdf 
    
def binarieToDecimal(num):
    # Lo convertimos en array para recorrer y sumar 2**indice
    newNum = []
    for x in str(num):
        newNum.append(int(x))
    # Invertimos el numero para ir sumando las potencias de 2 en orden (1,2,4 etc)
    arrayDelNumero = newNum[::-1]
    # Declaro la respuesta en 0 como un acumulador
    response = 0
    print(arrayDelNumero)
    for i in range(0,len(arrayDelNumero)):
        if (int(arrayDelNumero[i]) == 1): # Si el valor en el array es 1 lo sumamos 
            response = response + 2**i
    return response

print("El  en decimal es", binarieToDecimal(11001010))

        