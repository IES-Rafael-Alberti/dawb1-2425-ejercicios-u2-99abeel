def comprobar_numero(edad: int) -> bool:
    try:
        int(edad)
    except ValueError:
        print("**ERROR**")
        return False
    return True    
   


def main():
    edad = input("Escribe tu edad: ")
    if comprobar_numero(edad) == True:
        edad = int(edad)
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")


if __name__ == "__main__":
    main()

