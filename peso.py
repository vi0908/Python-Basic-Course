masa = float(input("amigo, ¿cuánto masas? "))
gravedad = 9.81
peso = float(masa * gravedad)
peso = round(peso, 2)
if peso > 500:
    peso = str(peso)
    print ("amigo, tu peso es de : " + peso + " N !woah¡ si que pesas xdxd" )
else:
    peso = str(peso)
    print ("xd")