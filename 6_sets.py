### Sets ###
# Es un conjunto, es decir una colección de elementos únicos y desordenados

my_set = set()
my_other_set = {}

print(type(my_set)) # Imprime el tipo de dato de "my_set", que es "set"
print(type(my_other_set)) # Imprime el tipo de de "my_other_set", que es "set"

var1 = {"Hola", "Mundo", 34}
print(type(var1))

# Añadir valores de una variable
var1.add("Qué tal")
print(var1)

var1.add("Hola")
print(var1)

# Eliminar valores de una variable
var1.remove("Hola")
print(var1)

# Búsqueda de elemento en el set (Conjunto)
print("Mundo" in var1)

# Tranformación de set a lista

var2 = list(var1)
print(var2)

# Unión
my_other_set = {"kotlin", "Swift", "Python"}
my_other_languages= {"php", "Css"}

var_unio = my_other_set.union(my_other_languages).union({"JavaScript", "C#", "C++"})

print(var_unio)

# Diferencia
my_other_set_languages = {"JavaScript", "C#"}

print(var_unio.difference(my_other_set_languages))

