def precio(edad:int):
    if edad <= 4:
        print(f"La entrada es gratis, tienes {edad} años")
    elif edad > 4 and edad <= 18:
         print(f"La entrada son 5€, tienes {edad} años")
    elif edad > 18:
         print(f"La entrada son 10€, tienes {edad} años")
    else:
         print("Error.")
    
def comprobar_edad(edad) -> int:
    try:
        int(edad)
    except ValueError:
        print("Error, intentalo de nuevo")
        return False
    edad = int(edad)
    if edad < 0:
        print("La edad no puede ser negativa")
        return False
    elif edad > 100:
        print("La edad no puede ser mayor que 100")
        return False
    elif edad == 0:
        print("La edad no puede ser 0")
        return False
    else:
        return True
    
def main():
    edad = input("Dime tu edad: ")
    while comprobar_edad(edad) == False:
        edad = input("dime una edad valida: ")
    edad = int(edad)
    precio(edad)

if __name__ == "__main__":
    main()
     