#1
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres lo suficiente mayor para conducir")
elif edad<18:
 print("Eres menor de edad no puedes conducir")
else:
    menor_edad= 18 - edad
    print(f"Te faltan {menor_edad} años para aprender a conducir.")

#2
Mi_edad = 18
Tu_edad = int(input("Ingresa tu edad: "))
if Tu_edad > Mi_edad:
    diferencia = Tu_edad- Mi_edad
    print(f"Eres {diferencia} {'año' if diferencia == 1 else 'años'} mayor que yo.")
elif Tu_edad < Mi_edad:
    diferencia = Mi_edad- Tu_edad
    print(f"Soy {diferencia} {'año' if diferencia == 1 else 'años'} mayor que tú.")
else:
    print("Tenemos la misma edad.")

#3
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")
