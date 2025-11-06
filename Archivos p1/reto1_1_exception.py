def sumar(a,b):
    s=a+b
    print("La suma de ",a,"y",b,"es=",s)
    return sumar
def restar(a,b):
    s=a-b
    print("La resta de ",a,"y",b,"es=",s)
    return restar
def multiplicar(a,b):
    s=a*b
    print("El producto de ",a,"y",b,"es=",s)
    return multiplicar
#Este error es en caso de que exista una division por cero
def dividir(a,b):
    try:
        s = a / b
        print("La división entre", a, "y", b, "es =", s)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")


if __name__ == "__main__":
    while True: 
        print("\n=== Calculadora ===")
        print("| Sumar        1 |")
        print("| Restar       2 |")
        print("| Multiplicar  3 |")
        print("| Dividir      4 |")
        print("| Salir        5 |")

        try:
            opc = int(input("|--------------> "))
        except ValueError:
            print(" Error: debe ingresar un número entero (1-5).")
            continue  # En caso de un error vueleve al inicio del menu

        if opc == 5:
            print("Saliendo del programa...")
            break  # sale del bucle

        if opc < 1 or opc > 5:
            print("Opción inválida, intente de nuevo.")
            continue

        # Pedir los dos números con validación
        while True:
            try:
                num1 = float(input("Ingrese el primer número = "))
                num2 = float(input("Ingrese el segundo número = "))
                break  # si todo va bien, salir del bucle
            except ValueError:
                print("Error: debe ingresar solo números válidos.")

        # Realizar la operación seleccionada
        if opc == 1:
            sumar(num1, num2)
        elif opc == 2:
            restar(num1, num2)
        elif opc == 3:
            multiplicar(num1, num2)
        elif opc == 4:
            dividir(num1, num2)