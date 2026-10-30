print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n")

print("*** Ejercicio 10: Nivel de influencer ***")

#input() guarda texto; el usuario es texto, asi que no lo convertimos
usuario = input("\nTu usuario: @")
#int() convierte a numero entero para poder comparar
seguidores = int(input("¿Cuantos seguidores tienes?"))
#Si el usuario escribe 50000, ahora seguidores vale 50000

print(f"\n======= NIVEL DE @mar&regi ===============")

#PREGUNTA 1: ¿50000 es menor que 1000? Respuesta: False, pasa a la siguiente
if seguidores < 1000:
    print("Nivel: Principiante")

#PREGUNTA 2: si llegamos aqui, YA sabemos que tiene 1000 o mas 
#¿50000 es menor que 10000? Respuesta: False, pasa a la siguiente 
elif seguidores < 10000:
    print("Nivel: micorinfluencer")

#PREGUNTA 3: si llegamos aqui, ya sabemos que tiene 10000 o mas 
#¿50000 es menor que 100000? Respuesta: True, muestra el mensaje y TERMINA
elif seguidores < 100000:
    print("Nivel: Influencer")

#else: si ninguna fue True, tiene 100000 o mas 
else:
    print("Nivel: Celebridad digital")