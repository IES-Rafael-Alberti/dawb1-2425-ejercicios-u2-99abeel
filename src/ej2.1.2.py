contraseña = "hola123"

contraseña_pedida = input("Introduzca la contraseña: ")

if contraseña_pedida.lower() == contraseña.lower():
    print("Contraseña correcta!")
else:
    print("Contraseña incorrecta")
    
