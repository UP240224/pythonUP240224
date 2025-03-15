#1
Edades = [22, 19, 24, 25, 26, 24, 25, 24]
ConjEdades= set(Edades)
#2
print(len(Edades))
print(len(ConjEdades))
#3
if len(Edades)>len(ConjEdades):
 print("La lista de datos es mayor")
elif len(Edades)<len(ConjEdades):
 print("El conjunto de datos es mayor")
else:
 print("La lista y el conjunto de datos es igual") 
#4
print("cadena (String): secuencia de caracteres")
print("Lista (List):colección ordenada y modificable de elementos")
print("Tupla (Tuple):colección ordenada e inmutable de elementos")
print("Conjunto (Set):colección no ordenada y sin elementos duplicados")
#5
Texto="Soy profesor y me encanta inspirar y enseñar a las personas."

palabras= Texto.split()
print(palabras)
palabras_uni= set(palabras)
print(len(palabras_uni))



