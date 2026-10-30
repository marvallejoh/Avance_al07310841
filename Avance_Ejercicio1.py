print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n") 

print("*** Ejercicio 1: Estado de mi celular ***\n")

bateria = int(input("¿Cuanta bateria tienes? "))
espacio = int(input("¿Cuantos GB libres tienes? "))
notificaciones = int(input("¿Cuantas notificaciones sin leer tienes? "))

if bateria <= 20:
   print("Bateria baja, conecta tu cargador")

if espacio < 5:
   print("Poco espacio, borra fotos o apps que no uses")

if notificaciones > 0:
   print("Tienes", notificaciones, "notificaciones sin leer\n")
else: 
   print("Estas al dia, no tienes notificaciones\n")
