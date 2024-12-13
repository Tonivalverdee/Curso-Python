### Bucles ###

# While loop

my_condition = 0

# while True:
#     print(my_condition)
#     my_condition += 3
# else: # es opcional
#     print("Mi condición es mayor o igual a 10")

# while my_condition < 20:
#     my_condition += 1
#     if my_condition == 15:
#         print("Se cierra el programa")
#         break
#     print(my_condition)

# Tabla de multiplicar
# numero = int(input("Escribe un número entre el 0 y el 9: "))
# num = 1
# if numero < 10:
#     print("Tabla del número ", numero)
#     while numero <= numero*10:
#         resultado = num*numero
#         print(num, " x ", numero, " = ", resultado)
#         num += 1
    # if resultado == numero*10:
    #     break
# else:
#     print("Se ha producido un error")

# For
my_list = [12, 34, 45, 67, 80, 23, 6]

for item in my_list:
    print(item)

my_tupla = (12, 34, 45, 67, 80, 23, 6)

for item in my_tupla:
    item = item * 8
    print(item)

my_set = {12, 34, 45, 67, 80, 23, 6}

for item in my_set:
    item = item * 8
    print(item)

my_dict = {"Nombre": "Toni", 34 : "Hola"}

for item in my_dict:
    print(item)