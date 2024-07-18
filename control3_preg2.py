def es_binario(var):

    for x in var:

        if x != "0" and x != "1":
            return False

    return True    

var = input("Ingrese expresión: ")   
 
print()
print(es_binario(var))