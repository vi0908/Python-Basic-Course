def run():
    numero = int(input("Ingresa un numero para conocer sus divisores: "))
    contador = 1
    while contador <= 100:
       if contador % numero != 0:
           continue
       print(contador)
       contador = contador + 1

        

        
    # for contador in range(100):
    #     if contador % 4 != 0:
    #         continue
    #     print(contador)
    # texto = input("por favor ingresa un texto: ")
    # for caracter in texto:
    #     if caracter == "o":
    #       continue
    #     print(caracter)


if __name__=="__main__":
    run()