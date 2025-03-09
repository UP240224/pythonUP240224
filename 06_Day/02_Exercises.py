# Ejercicios: Nivel 2

# 6. Desempaquetar los hermanos y los padres de la tupla family_members
family_members="nombre de familia"
siblings_unpacking, father, mother = family_members[:-2], family_members[-2], family_members[-1],
print(f"Hermanos: {siblings_unpacking}, Padre: {father}, Madre: {mother},")

# 7. Crear tuplas de frutas, vegetales y productos animales. Unir las tres tuplas y asignarlas a una variable llamada food_stuff_tp.
fruits = ('Manzana', 'Banana', 'Naranja')
vegetables = ('Zanahoria', 'Tomate', 'Pepino')
animal_products = ('Leche', 'Queso', 'Carne')
food_stuff_tp = fruits + vegetables + animal_products
print(f"Tupla de alimentos: {food_stuff_tp}")

# 8. Cambiar la tupla food_stuff_tp a una lista llamada food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)
print(f"Lista de alimentos: {food_stuff_lt}")

# 9. Cortar el elemento o los elementos del medio de la tupla food_stuff_tp o la lista food_stuff_lt.
# Si la longitud es impar, cortamos el único elemento del medio, si es par, cortamos los dos elementos del medio.
middle_item = food_stuff_lt[len(food_stuff_lt) // 2] if len(food_stuff_lt) % 2 != 0 else food_stuff_lt[len(food_stuff_lt) // 2 - 1:len(food_stuff_lt) // 2 + 1]
print(f"Elemento(s) del medio: {middle_item}")

# 10. Cortar los primeros tres elementos y los últimos tres elementos de la lista food_stuff_lt.
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"Primeros tres elementos: {first_three}")
print(f"Últimos tres elementos: {last_three}")

# 11. Eliminar completamente la tupla food_stuff_tp.
del food_stuff_tp
# Intentar imprimir food_stuff_tp ahora causará un error porque la tupla ha sido eliminada.
# print(food_stuff_tp)  # Esto causaría un error.

# 12. Comprobar si un elemento existe en una tupla:
# Comprobar si 'Estonia' es un país nórdico
nordic_countries = ('Finlandia', 'Suecia', 'Noruega', 'Dinamarca', 'Islandia')
is_estonia_nordic = 'Estonia' in nordic_countries
print(f"¿Estonia es un país nórdico? {is_estonia_nordic}")

# Comprobar si 'Islandia' es un país nórdico
is_iceland_nordic = 'Islandia' in nordic_countries
print(f"¿Islandia es un país nórdico? {is_iceland_nordic}")