#1
dog={}
dog["nombre"]= "Dobby"
dog["color"]="Negro"
dog["raza"]="Golden"
dog["patas"]=4
dog["Edad"]=2
#2
Estudiante={
"Nombre":"Ely",
"Apellido":"Guardado",
"Genero":"Femenino",
"Edad": 18,
"Estado civil": "Soltera",
"Habilidad":" núemeros, mecánica",
"Estado": "Aguascalientes",
"City":"México",
"Dirección": "54 Moreno zaragoza"
}
#3
Long_estudi= len(Estudiante)
print(Long_estudi)
#4
Val_Habilidad= Estudiante["Habilidad"]
print(Val_Habilidad)
tipo=(type(Val_Habilidad))
#5
Nueva_habilidad=["habilidad"].append("memoria fotográfica")
Nueva_habilidad=["Habilidad"].append("trabajo en equipo")
print( Nueva_habilidad)
#6
listA=list(Estudiante.keys())
print(listA)
#7
val_listA=list(Estudiante.values())
print(val_listA)
#8
tuplas_listA= list(Estudiante.items())
print(tuplas_listA)
#9
del Estudiante["Dirección"]
print(Estudiante)
#10
del Estudiante
print(" el diccionario esta eliminado")
