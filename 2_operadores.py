### Operadores Aritméticos ###

# Operadores de enteros

# Definir variables

numero1=2
numero2=4

# Suma
print (numero1 + numero2)
# Resta
print (numero1 - numero2)
# Mutiplicación
print (numero1 * numero2)
# División
print (numero1 / numero2)
# Módulo
print (numero1 % numero2)
# División entera (sin decimales)
print (numero1 // numero2)
# Exponente
print (numero1 ** numero2)

# Combinar operadores
print (2**3 - 7 / 1 // 4)

# Operaciones con texto (Concatenacion)
print ("Hola" + " " + "Mundo")

# print ("Hola" + 5) Tira Error porque 5 es número y hola es texto
print ("Hola" + " " + str(5))
print ("Hola" * 5)
print ("Hola " * (3 ** 5))

my_float = 2.5 * 2

print (type(my_float)) # Es float porque predomina el float en la multiplicación
# print ("Hola " * my_float)
print ("Hola " * int(my_float)) # Al definirle que sea te tipo integer la variable, se convierte en entero

### Operadores comparativos ###

print (3 > 4) # Compara si 3 es mayor que 4. Imprime: False
print (3 < 4) # Compara si 3 es menor que 4. Imprime: True
print (3 >= 4) # Compara si 3 es mayor o igual que 4. Imprime: False 
print (3 <= 4) # Compara si 3 es menor o igual que 4. Imprime: True
print (3 <= 3) # Compara si 3 es menor o igual que 3. Imprime: True
print (4 >= 4) # Compara si 4 es mayor o igual que 4. Imprime: True
print (3 == 4) # Compara si 3 es igual que 4. Imprime: False
print (3 != 4) # Compara si 3 es diferente que 4. Imprime: True
print (numero1 != numero2) # Compara si la variable numero1 es diferente de la variable numero2. Imprime: True