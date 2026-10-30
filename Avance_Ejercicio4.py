print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n")

print("*** Ejercicio 4 MIS ESTADISTICAS ***\n")

usuario = input("¿Cual es tu usuario?")
seguidores = int(input("¿Cuantos seguidores tienes?"))
likes = int(input("¿Cuantos likes tuvo tu ultimo video?"))

if seguidores >= 1000:
    print("Ya puedes hacer lives")
else: 
    print("Te faltan", 1000 - seguidores, "seguidores para hacer lives")

if likes > seguidores:
    print("¡Tu ultimo video se hizo viral!\n")
else:
    print("Sigue publicando, vas bien\n")