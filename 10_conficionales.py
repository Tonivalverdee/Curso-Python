### Condicionales ###

#if

my_condition = False

if my_condition:
    print("Se ejecuta  la condición if")

# if, elif, else
my_condition = 5 + 6
if my_condition > 10 and my_condition < 20:
    print("El número es mayor a 10 y menor a 20")
elif my_condition == 25:
    print("El número es igual a 25")
else:
    print("El número no cumple con las condiciones")

print("------------------------------------------------")
print("Dame un número, no letras")
num = int(input("Dame un número, no letras: "))

if num > 10 and num < 20:
    print("El número es mayor a 10 y menor a 20")
elif num == 25:
    print("El número es igual a 25")
else:
    print("El número no cumple con las condiciones")

print("------------------------------------------------")
