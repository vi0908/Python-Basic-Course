
def es_primo(numero):
    contador = 0 
    for i in range(1, numero + 1):
        if numero == 1:
            contador += 1
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
          contador += 1
    if contador == 0:
        return True
    else:
        return False



def run():
    numero = int(input("por favor ingresa un numero:"))
    if es_primo(numero) == True:
      print("es primo")
    else:
        print("no es primo")

if __name__ == "__main__":
    run()
# numero = int(input("por favor ingresa un numero para conocer si es primo o no: "))
# for i in range(numero):
#     resto = numero % i
#     if resto != 0:

#         print("no es primo")
#     else: 
#         numero = True
#         print("no es primo")
     