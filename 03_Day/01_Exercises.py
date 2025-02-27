import math

edad = 25  
altura = 1.75 
numero_complejo = 3 + 4j  

base = float(input("Ingresa la base: "))
altura_triangulo = float(input("Ingresa la altura: "))
area_triangulo = 0.5 * base * altura_triangulo
print(f"El área del triángulo es {area_triangulo}")

lado_a = float(input("Ingresa el lado a: "))
lado_b = float(input("Ingresa el lado b: "))
lado_c = float(input("Ingresa el lado c: "))
perimetro_triangulo = lado_a + lado_b + lado_c
print(f"El perímetro del triángulo es {perimetro_triangulo}")

longitud = float(input("Ingresa la longitud: "))
anchura = float(input("Ingresa el ancho: "))
area_rectangulo = longitud * anchura
perimetro_rectangulo = 2 * (longitud + anchura)
print(f"Área del rectángulo: {area_rectangulo}, Perímetro: {perimetro_rectangulo}")

radio = float(input("Ingresa el radio: "))
pi = 3.14
area_circulo = pi * radio ** 2
circunferencia_circulo = 2 * pi * radio
print(f"Área del círculo: {area_circulo}, Circunferencia: {circunferencia_circulo}")

pendiente = 2  
interseccion_y = -2  
interseccion_x = -interseccion_y / pendiente
print(f"Pendiente: {pendiente}, Intersección en x: {interseccion_x}, Intersección en y: {interseccion_y}")

x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente_calculada = (y2 - y1) / (x2 - x1)
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Pendiente: {pendiente_calculada}, Distancia: {distancia}")

print(f"Comparación de pendientes: {pendiente == pendiente_calculada}")

def ecuacion_cuadratica(x):
    return x**2 + 6*x + 9

valores_x = [-3, -2, -1, 0, 1, 2]
for x in valores_x:
    y = ecuacion_cuadratica(x)
    print(f"x: {x}, y: {y}")

x_cero = -3  

print(len("python") != len("dragon"))

print("on" in "python" and "on" in "dragon")

oracion = "Espero que este curso no esté lleno de jerga"
print("jerga" in oracion)

print("on" not in "python" and "on" not in "dragon")

longitud_python = float(len("python"))
longitud_como_string = str(longitud_python)
print(f"Longitud como float: {longitud_python}, Como string: {longitud_como_string}")

numero = int(input("Ingresa un número: "))
print(f"{numero} es par: {numero % 2 == 0}")

#Comparacion
print(7 // 3 == int(2.7))
print(type("10") == type(10))
print(int(float('9.8')) == 10)

horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
salario = horas * tarifa
print(f"Tu salario semanal es {salario}")

anos_vividos = int(input("Ingresa los años que has vivido: "))
segundos_vividos = anos_vividos * 365 * 24 * 60 * 60
print(f"Has vivido {segundos_vividos} segundos.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
