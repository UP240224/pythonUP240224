# 1. Declarar una lista vacía
primera_l = []

# 2. Declarar una lista con más de 5 elementos
prim_lista= [13,23,45,67,8,0,45,]

# 3. Encontrar la longitud de la lista
long_lista = len(prim_lista)
print(f"La longitud de la lista es: {long_lista}")

# 4. Obtener el primer elemento, el elemento del medio y el último elemento de la lista
prim_elemento= prim_lista[0]
elem_med = prim_lista[len(prim_lista)//2]
ulti_elemento = prim_lista[-1]
print(f"Primer elemento: {prim_elemento}, Elemento del medio: {elem_med}, Último elemento: {ulti_elemento}")

# 5. Declarar una lista llamada mixed_data_types con varios tipos de datos
mixed_data_types = ['Ely','18','160','soltera','méxico']

# 6. Declarar una lista llamada it_companies con valores iniciales
Empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprimir la lista utilizando print()
print("Lista de empresas de TI:", Empresas)

# 8. Imprimir el número de empresas en la lista
print(f"El número de empresas en la lista es: {len(Empresas)}")

# 9. Imprimir la primera, la del medio y la última empresa
print(f"Primera empresa: {Empresas[0]}, Empresa del medio: {Empresas[len(Empresas)//2]}, Última empresa: {Empresas[-1]}")

# 10. Imprimir la lista después de modificar una de las empresas
Empresas[0] = 'Meta'
print(f"Lista después de modificar una empresa: {Empresas}")

# 11. Agregar una empresa de TI a it_companies
Empresas.append('Tesla')
print(f"Lista después de agregar una empresa: {Empresas}")

# 12. Insertar una empresa de TI en el medio de la lista de empresas
Empresas.insert(len(Empresas)//2, 'telcel')
print(f"Lista después de insertar una empresa en el medio: {Empresas}")

# 13. Cambiar el nombre de una de las empresas de it_companies a mayúsculas (¡excepto IBM!)
empresas_tec = [company.upper() if company != 'IBM' else company for company in Empresas]
print(f"Lista después de cambiar a mayúsculas: {empresas_tec}")

# 14. Unir las empresas de TI con una cadena '#; '
Empre_unid = ' #; '.join(Empresas)
print(f"Lista unida: {Empre_unid}")

# 15. Comprobar si una determinada empresa existe en la lista de it_companies
Exis_empresa = 'Google' in Empresas
print(f"¿Google está en la lista? {Exis_empresa}")

# 16. Ordenar la lista usando el método sort()
Empresas.sort()
print(f"Lista ordenada: {Empresas}")

# 17. Invertir la lista en orden descendente usando el método reverse()
Empresas.reverse()
print(f"Lista invertida: {Empresas}")

# 18. Cortar las primeras 3 empresas de la lista
prim_tres_empresas= Empresas[:3]
print(f"Las primeras tres empresas: {prim_tres_empresas}")

# 19. Cortar las últimas 3 empresas de la lista
últi_tres_empresas= Empresas[-3:]
print(f"Las últimas tres empresas: {últi_tres_empresas}")

# 20. Cortar la empresa o empresas del medio de la lista de empresas de TI
empresa_s_med =Empresas[len(Empresas)//2-1:len(Empresas)//2+2] if len(Empresas) % 2 == 0 else Empresas[len(Empresas)//2-1:len(Empresas)//2+1]
print(f"Empresas del medio: {empresa_s_med}")

# 21. Eliminar la primera empresa de TI de la lista
Empresas.pop(0)
print(f"Lista después de eliminar la primera empresa: {Empresas}")

# 22. Eliminar la empresa del medio de la lista de empresas de TI
Empresas.pop(len(Empresas)//2)
print(f"Lista después de eliminar la empresa del medio: {Empresas}")

# 23. Eliminar la última empresa de TI de la lista
Empresas.pop(-1)
print(f"Lista después de eliminar la última empresa: {Empresas}")

# 24. Eliminar todas las empresas de TI de la lista
Empresas.clear()
print(f"Lista después de eliminar todas las empresas: {Empresas}")

# 25. Destruir la lista de empresas de TI
del Empresas
# print(it_companies)  # Esto causaría un error porque la lista ya ha sido destruida

# 26. Unir las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(f"Lista unida de Front-End y Back-End: {full_stack}")

# 27. Copiar la lista unida y agregar Python y SQL después de Redux
copia_LU = full_stack.copy()
copia_LU.insert(copia_LU.index('Redux') + 1, 'Python')
copia_LU.insert(copia_LU.index('Python') + 1, 'SQL')
print(f"Lista después de agregar Python y SQL: {copia_LU}")

