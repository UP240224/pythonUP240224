#1
import random
import string
def generar_id_usuario():
    caracteres = string.ascii_letters + string.digits
    id_usuario = ''.join(random.choices(caracteres, k=6))
    return id_usuario
print(generar_id_usuario())
#2
def usuario_id_gen_by_user():
    Id = []
    cantidad_caracteres = int(input("Introduce la cantidad de caracteres para el ID: "))
    cantidad_ids = int(input("Introduce la cantidad de IDs a generar: "))
    caracteres = string.ascii_letters + string.digits
    for i in range(cantidad_ids):
        id_usuario = ''.join(random.choices(caracteres, k=cantidad_caracteres))
        Id.append(id_usuario)  
        print(f"ID {i + 1}: {id_usuario}")
    return Id 
usuario_id_gen_by_user()
#3
def rgb_color_gen():
    RED = random.randint(0,255)
    GREEN=random.randint(0,255)
    BLUE=random.randint(0,255)
    return f'RGB({RED},{GREEN},{BLUE})'
print(rgb_color_gen())


