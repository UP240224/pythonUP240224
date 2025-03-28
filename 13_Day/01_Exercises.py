#1
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
resultado=[num for num in numeros if num<=0]
print(resultado)
#2 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
Resultado = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(Resultado)
#3
result = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
RESULTADO= [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]
print(RESULTADO)
#5
Diccionario= [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(Diccionario)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
cadenas_concat = [f"{name[0][0]} {name[0][1]}" for name in names]
print(cadenas_concat)
#7
pendiente= lambda x1,y1,x2,y2: (y2-y1) / (x2-x1)
interseccion_y = lambda x1, y1, m: y1 - m * x1

x1,y1= 5, 9
x2,y2= 4, 7

m=pendiente(x1,y1,x2,y2)
print(m)
inter= interseccion_y(x1,y1,m)
print(inter)

