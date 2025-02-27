#'programacion en python'
Nombre="Ely Noemí"
Apellido="Guardado Jaáuregui"
NombreCompleto="Ely Noemí Guardado Jáuregui"
País="México"
Ciudad="Aguascalientes"
Edad=18
Año=2025
Is_Married="NO"
Is_true="Es verdadero"
color, complexión, edad="Morado","Delgada",18

#.
print(type(Nombre))
print(type(Apellido))
print(type(NombreCompleto))
print(type(País))
print(type(Ciudad))
print(type(Edad))
print(type(Año))
print(type(Is_Married))
print(type(Is_true))
print(type(color))
print(type(complexión))
print(type(edad))
print(len(Nombre))
print(len(Nombre)>len(Apellido))

num_uno, num_dos= 5,4
total=num_uno+num_dos
diff=num_uno-num_dos
producto=num_dos*num_uno
división=num_uno/num_dos
remainder=num_dos%num_uno
exp=num_uno**num_dos
floor_division=num_uno//num_dos
radio=30 
area_del_circulo=3.1416*(radio**2)
circunferencia_del_circulo=2*3.1416*radio
radio=float(input("ingrese el radio del círculo: "))
area=3.1416*(radio**2)
print(f"El area de circulo es:{ area}")

Nombre=input('Ingresa tu nombre:')
Apellido=input("ingresa tu apellido:")
Edad=input("ingresa tu edad:")
País=input("ingresa tu país:")
print(f"mi nombre es:{Nombre} {Apellido}, tengo{Edad} años y soy de {País}")
import keyword
print(keyword.kwlist)
