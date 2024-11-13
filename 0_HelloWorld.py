### Hola Mundo ###
# Nuestro hola mundo en Python
print("Hola Python") #Imprime la cadena de texto "Hola python" en la consola
print('Hola Python') #También imprime la cadena de texto "Hola python", pero usando comillas simples

# Esto es un comentario
# Los comenatrios en Python comienzan con el símbolo '#' y no son ejecutables por el programa

"""
Este es un
comenatario
en varias líneas
"""
# Este bloque entre comillas triploes es un comentario o texto de varias líneas. Aunque realmente es una cadena
# Se utiliza frecuentemente como comentarios de múltiples líneas.

'''
Este también es un
comenatrio en varias líneas
'''
# Similar al comentario anterior, este es un comentario de varias líneas usando comiddas simples triples.

# Cómo consultar el tipo de dato
print(type("Soy un dato str")) # La función type() devuelve el tipo de dato. Aquí imprime que el tipo es 'str' (cadena de texto)
print(type(5)) # Imprine el tipo 'int' (entero) del número 5
print(type(1.5)) # Imprime el tipo 'float' para el número decimal 1.5
print(type(3 + 1j)) # Imprime el tipo 'complex' (número complejo) para el valor 3 + 1j
print(type(True)) # Imprime el tipo 'bool' (boleano) para el valor True

print(type(print("Mi cadena de texto"))) # Primero imprime "Mi cadena de texto".
# Luego, la función print() no retorna ningún valor (retorna None), y type() imprime que ese valor es de tipo 'NoneType'.