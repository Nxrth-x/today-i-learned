# Exemplo 4 - Extendendo os objetos do Python

class sList(list):
    def __init__(self, *value):
        super().__init__(value)
    
    def map(self, callback):
        return [callback(value) for value in self]

    def filter(self, callback):
        return [value for value in self if callback(value)]

    def reduce(self, callback, initial = 0):
        for i in range(len(self)):
            initial = callback(initial, self[i])
        return initial

    def for_each(self, callback):
        [callback(value) for value in self]


lista = sList(1, 2, 3)
print(f"Original: {lista}")

# Map
print(f"Lista multiplicada por 2: {lista.map(lambda x: x * 2)}")

# Filter
print(f"Lista de números pares: {lista.filter(lambda x: x % 2 == 0)}")

# Reduce
print(f"Soma de todos os números da lista: {lista.reduce(lambda acc, nxt: acc + nxt)}")

# For each
print("For each")
lista.for_each(lambda x: print(x))