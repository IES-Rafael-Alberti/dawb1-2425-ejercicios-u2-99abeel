def preguntar_edad(edad) -> int:
    edad  = input("Dime tu edad: ") 
    if comprobar_numero(edad) == False:
        edad = preguntar_edad()
    return (edad)

def comprobar_numero(edad) -> bool:
    try:
        int(edad)
        edad = int(edad)
        test_edad(edad)
    except ValueError as e:
        if edad is None:
            print("Error, el numero que has introducido no es valido.")
            return False
        else:
            print(f"ERROR, {e}. Intentalo de nuevo.")
            return False
    return True

def test_edad(edad):
    if edad == 0:
        raise ValueError("La edad no puede ser 0")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 16:
        print("Eres menor de edad, no puedes tributar")
        raise SystemExit
    if edad > 100:
        raise ValueError("La edad no puede ser superior a 100")
    
def pedir_ingresos() -> int:
    ingresos = input("Dime tus ingresos mensuales ")
    if comprobar_ingresos(ingresos) == False:
        ingresos = pedir_ingresos()
    return (ingresos)

def comprobar_ingresos(ingresos) -> bool:
    try:
        int(ingresos)
        ingresos = int(ingresos)
        test_ingresos(ingresos)
    except ValueError as e:
        if ingresos is None:
            print("Error, el numero que has introducido no es valido.")
            return False
        else:
            print(f"Error, {e}. intentalo de nuevo")
            return False
    return True

def test_ingresos(ingresos):
    if ingresos < 0:
        raise ValueError("Los ingresos no pueden ser negativos")
    if ingresos < 1000:
        print("Los ingresos no pueden ser menor que 1000.")
        raise SystemExit
    

def main():
    edad = None
    ingresos = None
    while edad is None:
        edad = preguntar_edad()
    while ingresos is None:
        ingresos = pedir_ingresos()
    print(f"Como tienes {edad} años y {ingresos} euros mensuales puedes tributar")

    
    if __name__=="__main__":
        main()

