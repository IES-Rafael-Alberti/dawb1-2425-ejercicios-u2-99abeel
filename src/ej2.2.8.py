
def obtener_numero():
    numero = input("Introduce un número: ")
    try:
        int(numero)
    except ValueError:
        print("ERROR, introduce otro numero")
        return False
    if comprobar_negativo(numero) == False:
        return False
    return numero

def comprobar_negativo(numero:str) -> bool :
    if numero.startswith("-"):
        print("No se pueden usar numeros negativos, intentalo de nuevo")
        return False

def par(numero) -> bool:
    if numero % 2 ==0:
        return True
    elif numero % 2 == 1:
        return False










def main():
    numero = obtener_numero()
    while numero == False:
        numero = obtener_numero()
    crear_triangulo(numero)



if __name__ == "__main__":
    main()