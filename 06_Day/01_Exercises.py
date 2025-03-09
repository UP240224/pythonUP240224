# 1. Crear una tupla vacía
Primera_t= ()

# 2. Crear una tupla que contenga los nombres de tus hermanas y tus hermanos
# (puedes usar nombres imaginarios si no tienes hermanos reales)
Hermanos= ('David','Marcos')
Hermanas = ('Gaby','Ana')

# 3. Unir las tuplas de hermanos y hermanas y asignarlas a la variable siblings
siblings = Hermanos + Hermanas
print(f"Tupla de hermanos y hermanas: {siblings}")

# 4. ¿Cuántos hermanos y hermanas tienes?
num_siblings = len(siblings)
print(f"Tienes {num_siblings} hermanos y hermanas.")

# 5. Modificar la tupla siblings y agregar el nombre de tu padre y tu madre, luego asignarlo a la variable family_members
# Nota: Las tuplas son inmutables, por lo que no podemos modificar directamente una tupla. Necesitamos crear una nueva.
Padre = 'Gabriel'
Madre = 'Lourdes'
family_members = siblings + (Padre, Madre)
print(f"Tupla con miembros de la familia: {family_members}")


