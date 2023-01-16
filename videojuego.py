import random

def run():
    numero_aleatorio = random.randint(1, 50)
    numero_elegido = int(input("Por favor ingrese un número del 1 al 50-> "))
    vidas = 4
    while vidas > 0:
        while numero_aleatorio != numero_elegido:
            if numero_elegido < numero_aleatorio:
                print("Por favor, ingrese un número mayor ")
                vidas -= 1
            else:
                print("Ingrese un número menor ")
                vidas -=1
            numero_elegido = int(input("-> " ))
            if vidas == 0:
                print("¡Pardiez! No sirve para esto señora...")
                break
    if numero_aleatorio == numero_elegido:
        print("¡Eh! Has acertado, congratulaciones")



if __name__ == "__main__":
    run()