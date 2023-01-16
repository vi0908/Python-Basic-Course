import random

def generar_contrasena():
    mayusculas =["A", "B", "C", "D", "E", "F", "G"]
    minusculas =["a", "b", "c", "d", "e", "f", "g"]
    simbolos = ["¿", "$"]
    numeros = ["1", "2", "3"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena)
    return contrasena 

def run():
    contrasena = generar_contrasena()
    print("Su nueva contraseña es: " + contrasena)

if __name__== "__main__":
    run()