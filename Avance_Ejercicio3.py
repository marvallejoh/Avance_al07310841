
print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n") 

print("*** Ejercicio 3 WI-FI DEL CAFE ***\n")

contraseña_cafe = "Mochi_Latte_2026"

nombre = input("¿Como te llamas? ")
constraseña = input("Escribre la contraseña: ")
gasto = float(input("¿Cuanto gastaste?"))

if constraseña == contraseña_cafe:
    print("Conectado al WI-FI, bienvenida", nombre)
else:
    print("Contraseña incorrecta")

if gasto >= 100:
    print("Tienes 1 hora de Wi-Fi\n")
else:
    print("Tienes 30 minutos de Wi-Fi\n")