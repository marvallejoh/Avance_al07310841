print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n") 

print("*** Ejercicio 2 CREA TU CUENTA ***\n")

nombre = input("¿Como te llamas?")
anio = int(input("¿En que año naciste? "))
red_social = input("¿Cual es tu red social favorita?")

edad = 2026 - anio
print(nombre + ", tienes", edad, "años")

if edad >= 13:
    print("Tu cuenta en", red_social, "fue creada")
else:
    print("Todavia no puedes crear tu cuenta, te faltan", 13 - edad, "años")

if edad >= 18:
    print("Compras dentro de la app activadas\n")
else:
    print("Compras dentro de la app desactivadas\n")
