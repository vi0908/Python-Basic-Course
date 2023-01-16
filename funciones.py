opcion = int(input("Buenas tardes, por favor selecciona una opción: 1, 2, 3"))
def conversacion(mensaje, linea2):
    print(mensaje)
    print(linea2)
if opcion == 1:
    conversacion("has escogido el camino incorrecto", "por favor selecciona otra opción")
    opcion = int(input("Buenas tardes, por favor selecciona una opción: 1, 2, 3"))
    conversacion()
elif opcion == 2:
    conversacion("te has vuelto a equivocar", "por favor selecciona otra opción")
elif opcion == 3:
    conversacion("amigo pls", "seriedad x favor")
else:
    print("ahora si xd")