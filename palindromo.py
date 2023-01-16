def run ():
    palabra = str(input("ingrese una palabra: ")).lower().replace(" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
      print("es palíndromo 😃")
    else:
      print("no es palíndromo😞")

if __name__=="__main__":
    run()

