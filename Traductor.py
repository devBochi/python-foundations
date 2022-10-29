paresDeClaves = input("Ingrese sus pares de palabra:traduccion separados por ',' para crear el diccionario:\n").lower()

def creadorDeDiccionario(pares):
    traducciones = {}
    arrayDePares = pares.split(',')
    print(arrayDePares)
    for par in arrayDePares:
        parSeparado = par.split(':')
        traducciones[parSeparado[0]] = parSeparado[1]
    print(traducciones)
    return traducciones

diccionario1 = creadorDeDiccionario(paresDeClaves)
fraseParaTraducir = input('Ingrese a continuacion la frase en español que quiere traducir\n').lower()

def traductor(frase,diccionario):
    arrayDePalabras = frase.split(' ')
    print(arrayDePalabras)
    fraseTraducida = []
    for palabra in arrayDePalabras:
        if palabra in diccionario:
            fraseTraducida.append(diccionario[palabra])
        else:
            fraseTraducida.append(palabra)
    fraseFinal = " ".join(fraseTraducida)
    return fraseFinal

fraseTraducida = traductor(fraseParaTraducir,diccionario1)
print(fraseTraducida.capitalize())