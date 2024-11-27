### Tuplas ###

# Dos formas de declarar una tupla
my_tuple = tuple()
my_other_tuple = ()

my_tuple = "hola"
my_other_tuple = 3

# Imprimir las tuplas definidas posteriormente
var1 = (34,45,45)
var2 = (34,45,45, "hola", "mundo")

print(var1)
print(var2)
print(my_tuple)
print(my_other_tuple)
print(type(my_tuple))
print(type(my_other_tuple))

# Accesos a información de la tupla
print(var1[0]) # Acceso al primer valor
print(var1[-1]) # Acceso al último valor
# print(var1[4]) # Acceso al quinto valor -> Tira un error porque no hay 5 valores
# print(var1[-6]) # Acceso al sexto valor empezando por el tinal -> Tira un error porque no hay 6 valores

# Concatenación de tuplas
var3 = ("Hola", "Mundo")
var4 = (":", "Dime tu edad")
var5 = var3 + var4 # Concatenamos las dos variables definidas anteriormente
print(var5) 

# Dividir tuplas
var6 = var5[0:2] # De esta forma definimos los dos primeros valores mediante un rango

print(var6)

# Ver índices de contenido de una tupla
print(var5.index("Hola"))
print(var5.index("Mundo"))

# Contar veces que se repite un valor en una tupla
print(var5.count("Hola"))
print(var5.count("Mundo"))

# Convertir de tupla a lista y de lista a tupla
var5 = list(var5)
print(type(var5))
print(var5)

var5.append("23")

print(var5)

var5 = tuple(var5)
print(type(var5))
print(var5)
