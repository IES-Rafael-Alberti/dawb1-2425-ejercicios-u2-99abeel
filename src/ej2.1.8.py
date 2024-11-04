def comprobar_puntuacion(numero):
    sueldo = 2400
    numero = float(numero)
    if numero == 0.0:
        total = sueldo * numero
        print(f"Tienes un nivel inacpetable, vas a recibir {total}")
    elif numero == 0.4:
        total = sueldo * numero
        print(f"Tienes un nivel aceptable, vas a recibir {total}")
    elif numero == 0.6:
        total = sueldo * numero
        print(f"Tienes un nivel aceptable, vas a recibir {total}")
    else:
        print("Esta puntuacion es invalida, intentalo de nuevo")
        return False
    
def comprobar_numero(numero) -> bool:
    try:
        float(numero)
    except ValueError:
        print("Error, intentalo de nuevo.")
        return False
    return True

def main():
    numero = input("Dime tu puntuacion: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    while comprobar_puntuacion(numero) == False:
        numero = input("Dame una puntuación valida: ")
        comprobar_numero(numero)

if __name__ == "__main__":
    main()