
def dividir(numerador, divisor):
    if divisor == 0:
        return None
    return numerador / divisor
    

def main():
    try:
        num1 = float(input("Introduce un numero: "))
        num2 = float(input("Introduce otro numero para dividirlo: "))

        resultado = dividir(num1, num2)

        if resultado is None:
            print("Error, no se pueden dividir entre 0")
        else:
            print(f"El resultado es {resultado}")
    
    except ValueError:
        print("Error, numeros no validos")


if __name__=="__main__":
    main()