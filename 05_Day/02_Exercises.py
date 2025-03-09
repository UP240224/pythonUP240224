# Ejercicios Nivel 2
Edades= [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Ordenar la lista y encontrar la edad mínima y máxima
Edades.sort()
m_Edad= Edades[0]
M_Edad= Edades[-1]
print(f"Edad mínima: {m_Edad}, Edad máxima: {M_Edad}")

# 2. Agregar nuevamente la edad mínima y la edad máxima a la lista
Edades.append(m_Edad)
Edades.append(M_Edad)
print(f"Lista de edades después de agregar mínimo y máximo: {Edades}")

# 3. Encontrar la edad media
Edad_med = (Edades[len(Edades)//2] if len(Edades) % 2 != 0 else (Edades[len(Edades)//2 - 1] + Edades[len(Edades)//2]) / 2)
print(f"Edad media: {Edad_med}")

# 4. Encontrar el promedio
E_prom = sum(Edades) / len(Edades)
print(f"Promedio de edades: {E_prom}")

# 5. Encontrar el rango de edades
E_ran= M_Edad - m_Edad
print(f"Rango de edades: {E_ran}")

# 6. Comparar (min - promedio) y (max - promedio)
compare = abs(m_Edad - E_prom) == abs(M_Edad - E_prom)
print(f"¿(min - promedio) es igual a (max - promedio)? {compare}")

# 7. Encontrar el país o países del medio
Paises= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
País_es = Paises[len(Paises)//2]
print(f"País del medio: {País_es}")

# 8. Dividir la lista de países en dos mitades
mitad = len(Paises) // 2
if len(Paises) % 2 == 0:
    Primera_mit = Paises[:mitad]
    segunda_mit = Paises[mitad:]
else:
    Primera_mit = Paises[:mitad + 1]
    segunda_mit = Paises[mitad + 1:]
print(f"Primera mitad: {Primera_mit}, Segunda mitad: {segunda_mit}")

# 9. Desempaquetar los tres primeros países
primeros_tres, *paises_escandinavos= Paises
print(f"Primeros tres países: {primeros_tres}, Países escandinavos: {paises_escandinavos}")
