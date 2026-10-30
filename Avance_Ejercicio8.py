print("\n*** Mariana Vallejo:     Matricula: al07310841     ***")
print("*** Regina Crispin:     Matricula: al07287967     ***\n")

print("*** Ejercicio 8:  CUENTA ENTRE AMIGOS ***")

cuenta = float(input("¿Cuanto fue la cuenta? "))
personas = int(input("¿Cuantas personas van a pagar? "))
dinero = float(input("¿Cuanto dinero traes? "))

propina= cuenta * 10 / 100
total = cuenta + propina
por_persona = total / personas 

print("Total con propina: $", total, sep="")
print("A cada persona le toca: $", por_persona, sep="")

if dinero >= por_persona: 
    print("Te alcanza, te sobran $", dinero - por_persona, sep="")
else:
    print("No te alcanza, te faltan $", dinero - por_persona, sep="")

if por_persona > 300:
    print("Salio caro, la proxima busquen promo\n")
else: 
    print("¡Buen precio!\n")
    