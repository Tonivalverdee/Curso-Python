### Calculadora ###

def mostrar_menu():
    print("------------------------")
    print("\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    var1 = int(input("Qué cálculo quieres hacer: "))
    print("\n")
    return var1

while True:
    var1 = mostrar_menu()
    if var1 == 1:
        print("Suma")
        print("------------------------")
        print("\n")
        sum1 = int(input("Dame un primer número a sumar: "))
        sum2 = int(input("Dame un segundo número a sumar: "))
        print("\n")
        print("El resultado de la suma es: ", sum1+sum2)
        print("\n")
        print("Pulsa enter para continuar")
        input()
    if var1 == 2:
        print("Resta")
        print("------------------------")
        print("\n")
        print("\n")
        rest1 = int(input("Dame un número que quieres restar: "))
        rest2 = int(input("Dame un número con el que quieres restar: "))
        print("El resultado de la resta es: ", rest1-rest2)
        print("\n")
        print("Pulsa enter para continuar")
        input()
    if var1 == 3:
        print("Multiplicación")
        print("------------------------")
        print("\n")
        print("\n")
        mult1 = int(input("Dame un primer número a multiplicar: "))
        mult2 = int(input("Dame un segundo número a multiplicar: "))
        print("El resultado de la multiplicación es: ", mult1*mult2)
        print("\n")
        print("Pulsa enter para continuar")
        input()
    if var1 == 4:
        print("División")
        print("------------------------")
        print("\n")
        print("\n")
        div1 = int(input("Dame un número que quieres dividir: "))
        div2 = int(input("Dame un número con el que quieres dividir: "))
        if div2 == 0:
            print("No se puede dividir entre 0")
        else:
            print("El resultado de la división es: ", div1/div2)
            print("\n")
            print("Pulsa enter para continuar")
        input()
    if var1 == 5:
        break
    if var1 > 5:
        print("Opción no válida")
        print("\n")
        print("Pulsa enter para continuar")
        input()