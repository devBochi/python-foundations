# """
# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla la lista de la compra y el coste total, 
# con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste

# """
# import os               # para hacer el clear screen (no afecta el funcionamiento del programa)
# from time import sleep  # para esperar antes de limpiar pantalla

# # Seteamos las variables a utilizar
# salida = ''
# sum = 0
# carrito = {}

# print('\nBienvenido a la tienda, ingrese a continuacion el articulo que quiere comprar y su precio\n')
# sleep(4)
# # Loop para llenar el carrito de articulos
# while (salida != 'NO'): 
#     os.system('cls')
#     item = input("Nombre del articulo: ")
#     precio = int(input("Precio del articulo: "))
#     carrito[item] = {'Articulo':item,'Precio':precio} 
#     sum = sum + precio
#     salida = input("Desea seguir comprando? Ingrese SI o NO: ")
    
# os.system('cls')
# print("Lista de articulos:")
# for item in carrito:
#     print('-',carrito[item]["Articulo"],':',carrito[item]["Precio"],"USD")

# print('-----------------')
# print("Total:",sum,"USD")
# print("\nGracias por comprar en nuestra tienda!\n")

import subprocess

subprocess.run(['python','--version'])