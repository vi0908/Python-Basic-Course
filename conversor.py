mensaje = """
Buen día querido amigo, bienvenido al conversor de monedas, por favor seleccione una opción :
1. De pesos colombianos a chilenos 🧧
2. De pesos chilenos a colombianos 🧧
 """

proceso = int(input(mensaje))
pesos = float(input("Querido amigo: ¿cuántos pesos tiene? "))
valor_pesochileno = float(input("¿A cuánto está el peso chileno? (entendiendo que 1 peso chileno = x colombianos) "))

def conversion(operacion, mensaje_final):
     pesos = float(input("Querido amigo: ¿cuántos pesos tiene? "))
     valor_pesochileno = float(input("¿A cuánto está el peso chileno? (entendiendo que 1 peso chileno = x colombianos) "))
     peso_conversion= (operacion)
     peso_conversion= round(peso_conversion)
     peso_conversion = str(peso_conversion)
     print("Tiene: $" + peso_conversion + (mensaje_final))

if proceso == 1:
    conversion((pesos/valor_pesochileno), " pesos chilenos, ¡a de shopping!")
elif proceso == 2:
   conversion((pesos*valor_pesochileno), " pesos colombianos, ¡a de shopping!")
else:
    print("seriedad, por favor 🧧")





