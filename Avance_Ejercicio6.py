print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n")

print("*** Ejercicio 4 MI META DE AHORRO ***")

producto = input("¿Que quieres comprar? ")
precio = float(input("¿Cuanto cuestan? "))
ahorrado = float(input("¿Cuanto tienes ahorrado? "))
ahorro_semanal = float(input("¿Cuanto ahorra por semana? "))

if ahorrado >= precio:
    print("¡Ya puedes comprar tus", producto + "!")
else:
    faltante = precio - ahorrado
    semanas = faltante / ahorro_semanal
    print("Te faltan $", faltante, " para tus ", producto, sep="")
    print("Ahorrando $", ahorro_semanal, " por semana, los tendras en ", semanas, " semanas", sep="")
    print("\n")