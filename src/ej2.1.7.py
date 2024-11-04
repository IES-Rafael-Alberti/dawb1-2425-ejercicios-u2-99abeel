def renta(nuero):
    numero = float(numero)
    if numero < 10000:
        print ("Te corresponde un 5% de impositivo")
    elif numero >= 10000 and numero < 20000:
        print("Te corresopnde un 15% de impositivo")
    elif numero >= 20000 and numero < 35000:
        print("Te corresponde un 20% de impositivo")
    elif numero >= 35000 and numero < 60000:
        print("Te corresponde un 30% de impositivo")
    elif numero >= 60000:
        print("Te corresponde un 45% de impositivo")
    
def comprobar_numero(numero) -> bool:
    try:
        float(numero)
    except ValueError:
        print("Error, intentalo de nuevo")
        return False
    return True

def main():
    numero = input("Dime tus ingresos: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    renta(numero)


if __name__ == "__main__":
    main()
