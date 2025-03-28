#1
import random
def functions_of_hexa_colors(n):
    caracteres_hexa='0123456789abcdef'
    colores_hexa=[]
    for _ in range(n):
        color='#'+''.join (random.choices(caracteres_hexa, k=6))
        colores_hexa.append(color)

        return colores_hexa
print(functions_of_hexa_colors(5))
#2
def functions_of_rgb_colors(n):
    colores_rgb=[]
    for _ in range(n):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        color=f'rgb({red},{green},{blue})'
        colores_rgb.append(color)
        return colores_rgb
print(functions_of_rgb_colors(10))
#3
def generar_color_hexa():
    hex_chars = '0123456789abcdef'
    return '#' + ''.join(random.choices(hex_chars, k=6))

def generar_color_rgb():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f'rgb({red}, {green}, {blue})'

def generar_colores(tipo, cantidad):
    colores = []
    
    if tipo == 'hexa':
        for _ in range(cantidad):
            colores.append(generar_color_hexa())
    elif tipo == 'rgb':
        for _ in range(cantidad):
            colores.append(generar_color_rgb())
    else:
        raise ValueError("El tipo debe ser 'hexa' o 'rgb'")
    
    return colores

print(generar_colores('hexa', 5))
print(generar_colores('rgb', 3)) 

