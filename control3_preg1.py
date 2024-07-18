def digitos(num):

    cant = len(num)
    return cant

num = input("Ingrese número a elección: ")

if num.isdigit():

    print()
    print(f"El número ingresado tiene {digitos(num)} dígito/s")

else:
    
    print()
    print("El valor ingresado no puede ser procesado como número.")