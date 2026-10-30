print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n")

print("*** Ejercicio 16 Reto: arma tu bubble tea ***")

#===== DECISIÓN 1: EL TAMAÑO =====
print("\n===== TAMAÑOS =====")
print("1 = Chico ($55)   2 = Mediano ($78)   3 = Grande ($85)")
tamano = int(input("Elige tu tamaño: "))
#Si el usuario escribe 2, ahora tamano vale 2

#En cada opción guardamos el nombre y el precio del tamaño
if tamano == 1:
    nombre_tamano = "Chico"
    precio_bebida = 55
#¿2 es igual a 2? True, guarda Mediano y 78, y TERMINA este bloque
elif tamano == 2:
    nombre_tamano = "Mediano"
    precio_bebida = 78
elif tamano == 3:
    nombre_tamano = "Grande"
    precio_bebida = 85
#else: opción no válida, le damos chico
else:
    print("Opción no válida, te damos tamaño chico")
    nombre_tamano = "Chico"
    precio_bebida = 55

#===== DECISIÓN 2: EL TOPPING =====
#Este es OTRO bloque, Python lo revisa aunque el anterior ya haya terminado
print("\n===== TOPPINGS =====")
print("1 = Chispitas de amor ($15)   2 = Dulces de arcoiris ($12)   3 = Sin topping ($0)")
topping = int(input("Elige tu topping: "))
#Si el usuario escribe 1, ahora topping vale 1



#¿1 es igual a 1? True, guarda Perlas y 15, y TERMINA este bloque
if topping == 1:
    nombre_topping = "Chispitas de amor"
    precio_topping = 15
elif topping == 2:
    nombre_topping = "Dulces de arcoiris"
    precio_topping = 12
elif topping == 3:
    nombre_topping = "Sin topping"
    precio_topping = 0
else:
    print("Opción no válida, te dejamos sin topping")
    nombre_topping = "Sin topping"
    precio_topping = 0

#===== TOTAL =====
#Sin sangría: se hace SIEMPRE. Esta fórmula dice: total = 70 + 15
total = precio_bebida + precio_topping
#Ahora total vale 85

print("\n===== TU PEDIDO =====")
print(f"Tamaño: {nombre_tamano} ${precio_bebida}")
print(f"Topping: {nombre_topping} ${precio_topping}")
print(f"TOTAL: ${total}")