import math
#1
def add_two_numbers(num1, num2):
    return num1 + num2  
result = add_two_numbers(12, 34)  
print(result) 
#2

def area_of_circle(radio):
    pi=3.1416
    return pi* radio* radio
print(area_of_circle(15))
#3
def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números." 
result = add_all_nums(1, 2, 3, 4, 5)  
print(result)  

result_with_error = add_all_nums(1, 2, 'a', 4) 
print(result_with_error)  
#4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit 
celsius = 25
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")
#5
def check_season(month):
    if month in [12, 1, 2]:
        return "Invierno"
    elif month in [3, 4, 5]:
        return "Primavera"
    elif month in [6, 7, 8]:
        return "Verano"
    elif month in [9, 10, 11]:
        return "Otoño"
    else:
        return "Mes inválido"
mes = 3
estacion = check_season(mes)
print(f"El mes {mes} corresponde a la estación: {estacion}")
#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pendiente es indefinida (línea vertical)"
    slope = (y2 - y1) / (x2 - x1)
    return slope
x1, y1 = 1, 2
x2, y2 = 3, 6
slope = calculate_slope(x1, y1, x2, y2)
print(f"La pendiente de la recta es: {slope}")
#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales."
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return root1, root2
#8
def print_list(lst):
    for item in lst:
        print(item)
#9
def reverse_list(lst):
    return lst[::-1]
#10
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
#11
def add_item(lst, item):
    lst.append(item)
    return lst
#12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
#13
def sum_of_numbers(n):
    return sum(range(1, n+1))
#14
def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)
#15
def sum_of_even(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)
