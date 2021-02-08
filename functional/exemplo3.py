# Maps e filters

lista = [1, 2, 3]
lista_multiplicada = list(map(lambda x: x * 2, lista))

print(f"Lista multiplicada: {lista_multiplicada}")

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
lista_de_numeros_pares = list(filter(lambda x: x % 2 == 0, lista_de_numeros))

print(f"Lista de números pares: {lista_de_numeros_pares}")