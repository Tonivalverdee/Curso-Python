### Variables ###
my_string_variable = "My String Variable" # Se asigna una cadena de texto a la variable 'my_string_variable'
print(my_string_variable) # Imprime el valor de la variable 'my_string_variable', que es "My String Variable"

my_int_variable = 5 # Se asigna un número entero a la variable 'my_int_variable'
print(my_int_variable) # Imprime el valor de 'my_int_variable', que es 5

my_int_to_str_variable = str(my_int_variable) # Se convierte el número entero '5' a una cadena de texto y lo guarda en la variable 'my_int_to_str_variable'
print(my_int_to_str_variable) # Imprime el valor de 'my_int_to_str_variable', que ahora es "5" (cadena de texto)
print(type(my_int_to_str_variable)) # Imprime el tipo de dato de 'my_int_to_str_variable', que es 'str' (cadena)

my_bool_variable = False # Se asigna un valor booleano a la variable 'my_bool_variable'
print(my_bool_variable) # Imprime el valor de 'my_bool_variable', que es False

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable) 
# Imprime varias variables en una sola línea, separadas por espacios: "My String Variable 5 False"

print("Este es el valor de:", my_bool_variable)
# Imprime el texto y el valor de 'my_bool_variable': "Este es el valor de: False"

# Algunas funciones del sistema
print(len(my_string_variable))
# La funcion 'len()' devuelve la longitud de una cadena 'my_string_variable'. Aquí imprimirá 18, que es el número de caracteres en la cadena.

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Ruben", "Caravaca", 'brasombra', 51
# Se asignan múltiples variables en una sola línea. 'name' toma el valor de 'Ruben', 'surname' toma el valor de 'Caravaca', 'alias' toma el valor de 'brasombra', y 'age' toma el valor de 51.

print("Me llamo:", name, surname, ". Mi edad es:", age, ". Mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
# Pide al usuario que ingrese su nombre y almacena el valor en la variable 'name'

age = int(input('¿Cuántos años tienes? '))
# Pide al usuario que ingrese su edad y almacena el valor en la variable 'age'

print(name) # Imprime el nombre ingresado por el usuario
print(age) # Imprime la edad ingresada por el usuario

#Cambiamos su tipo
name = 51 # Ahora se reasigna un valor entero a la variable 'name' (antes era una cadena de texto)
age = "Ruben" # Ahora se reasigna un valor cadena a la variable 'age' (antes era un número entero)
print(name) # Imprime el valor de 'name', que ahora es 51
print(age) # Imprime el valor de 'age', que ahora es "Ruben"

# ¿Forzamos el tipo?
address: str = "Mi dirección"
# Se indica que la variable 'address' será de tipo 'str' (cadena de texto), pero Python no obliga a respetarlo.

address = True # Reasignamos un valor booleano a 'address'
address = 5 # Luego un valor entero
address = "1.2" # Finalmente un valor decimal
print(type(address)) 
# Imprime el tipo de dato de 'address', que ahora es 'float' (el último valor asignado es 1.2, que es un número decimal).