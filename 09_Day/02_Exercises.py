#1
puntaje = int(input("Ingresa tu puntaje: "))
if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje <= 89:
    print("Calificación: B")
elif 60 <= puntaje <= 69:
    print("Calificación: C")
elif 50 <= puntaje <= 59:
    print("Calificación: D")
else:
    print("Calificación: F")

#2
mes = input("Ingresa el mes: ").lower()
if mes in ["septiembre", "octubre", "noviembre"]:
    print("La temporada es Otoño.")
elif mes in ["diciembre", "enero", "febrero"]:
    print("La temporada es Invierno.")
elif mes in ["marzo", "abril", "mayo"]:
    print("La temporada es Primavera.")
elif mes in ["junio", "julio", "agosto"]:
    print("La temporada es Verano.")
else:
    print("Mes inválido.")

#3
frutas = ['plátano', 'naranja', 'mango', 'limón']
fruta = input("Ingresa una fruta: ").lower()
if fruta in frutas:
    print("Esa fruta ya existe en la lista.")
else:
    frutas.append(fruta)
    print(frutas)