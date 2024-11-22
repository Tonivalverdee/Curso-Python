### Lists ###

# Definición de listas vacías
my_list = list() # Crear una lista vacía usando el constructor list()
my_order_list = [] # Imprime una lista vacía usando []

print(len(my_list)) # Imprime la longitud de la lista, en este caso es 0
print(len(my_order_list)) # Imprime la longitud de la lista, en este caso es 0

# Definir una lista con valores
my_list = [35, 20, 40, 35, 14]

print(my_list) # Imprime la lista con valores
print(len(my_list)) # Imprime el número de valores

# Lista de tipos diferentes
my_type_list = ["Hola", 3, "Mundo", 1.88, 3]
print(my_type_list) 
print(len(my_type_list))

# Acceso a elementos de una lista
print(my_type_list[0]) # Accede al primer elemento
print(my_type_list[-1]) # Accede al último elemento
print(my_type_list[-4]) # Accede al primer elemento (4 para atrás)
print(my_type_list.count(3)) # Cuenta el número de elementos que se repiten del número 3

# Como buscar el el índice termino Hola el my_type_list = ["Hola", 3, "Mundo", 1.88, 3]
my_type_list = ["Hola", 3, "Mundo", 1.88, 3, "Hola"]
print(my_type_list.index("Hola"))

# Desempaquetar una lista
var1, var2, var3, var4, var5, var6= my_type_list

print(var1, var2, var3) 

var1, var2 = my_type_list[0], my_type_list[5]

print(var1, var2)

# Concatenar dos listas
list1 = ["Hola", 3, "Mundo"]
list2 = [1.88, 3, "Hola"]

print(list1 + list2)

list3 = list1 + list2

print(list3)

# CURL de elementos (Creación, Insertación, Actualización, Eliminación)

list3.append("Jorge") # Añade un elemento a la lista
print(list3)

list3.append(85) # Añade otro elemento a la lista, esta vez un número
print(list3)

list3.insert(3, "Jose") # Inserta en la cuarta posición Jose
print(list3)

list3.remove("Hola") # Elimina el primer término Hola
print(list3)

list3[0] = "Javier" # Actualiza la posición por el térmico indicado
print(list3)

resultado = list3.pop() # Elimina el último término de la lista y lo almacena en la variable nueva
print(list3)
print(resultado)

resultado = list3.pop(0) # Elimina el primer valor de la lista y lo almacena en la variable nueva
print(list3)
print(resultado)

del list3[1] # Elimina el valor del segundo puesto
print(list3)

list4 = list3.copy() # Hace una copia de una variable en otra

list3.clear() # Elimina todos los valores de la lista
print(list3)
print(list4)

list4.reverse() # Cambia el orden de los valores de la lista
print(list4)

listaInt = [45, 34, 12, 1, 56] # Creamos una nueva lista de números enteros
print(listaInt)

listaInt.sort() # Ordena la lista de números enteros de menor a mayor
print(listaInt) 

listaInt.sort(reverse=True) # Ordena la lista de números de mayor a menor
print(listaInt)

print(listaInt[1:3])

lista_string = "Hello, world!" # Creamos una nueva lista string
print(lista_string) 
print(type(lista_string)) # Pedimos el tipo de la lista, mostrará str de string