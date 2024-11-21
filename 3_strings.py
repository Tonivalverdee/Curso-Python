### Strings###

# Declaración de strings usando comillas simples y dobles
variable1 = 'Antonio'
variable2 = "Valverde"

print(variable1)
print(variable2)

# Concatenar strings con un espacio en blanco
print(variable1 + " " + variable2)

# Crear un salto de línea
variable3 = "Esto es un string\ncon salto de línea"
print(variable3)

# Insertar tabulación
variable4 = "\tEsto es un string con una tabulación"
print(variable4)

# Escapar caracteres especiales
variable5 = "\\tEsto es un string sin tabulación, ya que con la \ hago que esta tabulación no se haga"
print(variable5)

# Formateo de strings
name, surname, age = "Antonio", "Valverde", 19

# Formateo usando .format()
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))

# Formateo antiguo usando %
print("Mi nombre es %s %s y mi edad es %d"%(name,surname,age))

# Concatenar varios string
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

# Formateo usando f-strings (moderno)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetando caracteres
language = "Python"

a,b,c,d,e,f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División de caracteres (Slice)
language_slice = language[1:3]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

### Funciones de string ###

# Reemplazar caracteres de un string
fruit = "strawberry"
fruit_replace = fruit.replace("r", "R")
print(fruit_replace)

# Convertir el primer caracter del texto en mayúscula
print(fruit.capitalize())

# Convertir todo el texto en mayúscula
print(fruit.upper())

# Contar cuantos caracteres hay del mismo tipo
print(fruit.count("r"))

# Contar todos los caracteres de una palabra
print(len(fruit))

print(f"La variable {fruit} tiene: " + str(len(fruit)))

# Comprobar si todos los caracteres son numéricos
print(fruit)
print(fruit.isnumeric())

numero_de_letras = len(fruit)
print(numero_de_letras)
print(str(numero_de_letras).isnumeric())

# Convertir el texto a minúsculas
print(fruit.lower())

# Comprobar si todo el texto es en minuscula
print(fruit.islower())

# Comprobar si comienza la cadena con unos caracteres
# Ejemplo Py -> Python
print(language.startswith("Py"))