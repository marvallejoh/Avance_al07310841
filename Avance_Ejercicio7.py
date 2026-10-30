print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n")

print("*** Ejercicio 7: TIEMPO DE PANTALLA ***")

nombre = input("¿Como te llamas? ")
limite = float(input("¿Cual es tu limite de horas? "))
horas_redes = float(input("¿Cuantas horas en redes sociales? "))
horas_juegos =float(input("¿Cuantas horas en videojuegos? "))

total = horas_redes + horas_juegos
print(nombre + ", hoy usaste el celular", total, "horas")

if total > limite:
    print("Te pasaste", total - limite, "horas de tu limite, ¡es hora de desconectarte!")
else:
    print("¡Felicidades! Cumpliste tu meta de tiempo de pantalla")

if horas_redes > horas_juegos:
    print("Lo que mas usaste fueron las redes sociales\n")
else:
    print("Lo que mas usaste fueron los videojuegos\n")