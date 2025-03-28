#1
import random
def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list
mi_lista = [1, 2, 3, 4, 5, 6]
lista_mezclada = shuffle_list(mi_lista)
print("Lista original mezclada:", lista_mezclada)
#2
def generar_numeros_unicos():
    numeros = random.sample(range(10), 7)
    return numeros
numeros_aleatorios = generar_numeros_unicos()
print(numeros_aleatorios)

