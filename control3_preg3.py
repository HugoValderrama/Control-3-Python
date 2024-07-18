def potencia(num, exp):

    if exp == 0:
        return 1
    else:
        return num * potencia(num, exp - 1)    

num = int(input("Ingrese base: "))
exp = int(input("Ingrese exponente: "))

print()
print(f"El resultado es: {potencia(num, exp)}")