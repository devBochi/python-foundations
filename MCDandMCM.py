# Nahuel Montes de Oca - aws re/Start

# Escribir una funcion que 
# calcule el mcd y otra q calcule el mcm

def getMaxComDiv(a,b):
    response = 1 # Seteo la respuesta en 1 por si no encuentro otro divisor comun
    # Creo los arrays con los divisores de a y b
    aDivisors = [] 
    bDivisors = []
    # Agrego los divisores de cada uno en los arrays respectivos
    for i in range(1,int(a/2)):
        if ((a % i) == 0):
            aDivisors.append(i)
    for i in range(1,int(b/2)):
        if ((b%i) == 0):
            bDivisors.append(i)
    # Creo las condiciones para salir del while
    divisorFound = False
    if(a<b):
        cont = len(aDivisors)-1
    else:
        cont = len(bDivisors)-1
    #Si encuentro otro divisor o llego al principio del array salgo del while
    while ( (divisorFound != True) and (cont != 0) ): 
        if cont in bDivisors:
            response = cont
            divisorFound = True
        else:
            cont = cont - 1
    # Retorno la respuesta sea cual sea
    return response
                
print("The max common divisor is: ",getMaxComDiv(345,128))

def getMinComMultiple(a,b):
    # Definimos un rango para completar los arrays
    if (a>b):
        maxRange = b
    elif (a<b):
        maxRange = a
    else:
        return a
    # Creo los arrays con algunos multiplos de cada uno
    aMultiples = []
    bMultiples = []
    # Agrego los mutiplos de cada uno en los arrays respectivos
    # Para ahorrar tiempo si llego a a*b me salgo del for
    for i in range(1,maxRange):
        aMultiples.append(i*a)
        if i*a > a*b:
            break
    for i in range(1,maxRange):
        bMultiples.append(i*b)
        if i*b > a*b:
            break
    # Creo las condiciones para salir del while
    print(aMultiples)
    print(bMultiples)
    commonFound = False
    cont = 0
    maxR = len(aMultiples) - 1
    response = a*b # Seteo la respuesta como su producto siendo la primera opcion
    #Si encuentro otro multiplo o llego al principio del array salgo del while
    while ( ( cont < maxR ) and ( commonFound != True )):
        if aMultiples[cont] in bMultiples:
            response = aMultiples[cont]
            commonFound = True
        else:
            cont = cont + 1
    # Retorno la respuesta sea cual sea
    return response
    
    # print("The min common multiple is: ", getMinComMultiple(876,145))