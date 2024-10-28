def par(numero):
    return numero % 2 == 0

def main():
        try:
            numero = int(input("Introduce un numero: "))

        except ValueError:
            print("El numero que has introducido no es valido, introducelo de nuevo: ")

        if par(numero):
            print("Tu numero es par")
        else:
            print("Tu numero es impar")



if __name__=="__main__":
    main()