
def validar_edad(edad: int):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad == 0:
        raise ValueError("La edad no puede ser 0")
    if edad > 125:
        raise ValueError("La edad no puede ser superior a 125")
    
def pedir_edad() -> int:
    edad = None

    while edad == None:
        try: 
            edad = int(input("Introduzca su edad: "))
            
        except ValueError as e:
            if edad is None:
                print(f"El numero introducido no es valido. Intentalo de nuevo")
            else:
                print(f"*ERROR* {e}. Intentalo de nuevo.")

        return edad

def mostrar_anios_cumplidos (edad: int):
    for i in range (1, edad + 1):
        print(1)

def main():
    try:
        edad = int("Introduzca tu edad: ")
    except ValueError:
        print("*ERROR* edad no valida")

    for i in range (1, edad + 1):
        print(1)

if __name__=="__main__":
    main()