### Diccionario ###


my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # Imprime el tipo de dato de "my_dict", que es "dict"
print(type(my_other_dict)) # Imprime el tipo de dato de "my_other_dict", que es "dict"

# Definir un diccionario

my_dict = {
    "Nombre": "Toni",
    "Apellido": "Valverde",
    "Edad": 19,
    "Ciudad": "Cartagena",
    "Lenguages": {"JavaScript", "Python", "php"},
    1: {"Español", "Inglés"}
}

print(my_dict)
print(my_dict[1])
print(my_dict["Edad"])
# print("Toni" in my_dict) -> Da error, pese a ser un valor no es una clave
print("Toni" in my_dict["Nombre"])

# Insertar en un diccionario
my_dict["Calle"] = "Calle Bolnuevo"

print(my_dict)

# Actualizar una clave
my_dict["Calle"] = "Calle Isidoro"

print(my_dict)

# Eliminar una clave
del my_dict["Calle"]
print(my_dict)

# Operaciones con diccionarios
print("----------------------------------------------")
print(my_dict.items())
print("----------------------------------------------")
print(my_dict.keys())

# Creación de list
my_list = ["Nombre", 1, "Apellido"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

# Input de datos
# input1 = input()

# Output de datos
# print(input1)

print("----------------------------------------------")
print("Escribe un número, no escribas letras:")
num1 = int(input())

print("Me has dado el número: ", num1)