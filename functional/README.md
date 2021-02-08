# Today I Learned - Aplicação dos conceitos funcionais em Python 🐍

A programação funcional é um dos paradigmas de programação mais conhecidos e utilizados. Muitas linguagens vem aplicando conceitos da programação funcional como o `filters`, `maps`, imutabilidade e vários outros. Neste `Today I Learned` eu compilei algumas das coisas que eu venho aplicando na linguagem de programação `Python`.

## Funções puras

Funções puras são funções que não geram `side effects`, ou seja, não alteram variáveis já existentes. Funções puras são explicadas mais fácilmente demonstrando o que é uma função impura:

```Python
# Função impura
x = 5

def adicionar_cinco():
  x += 5

adicionar_cinco()

print(f"Exemplo de função impura: {x}")
```

> A função acima altera uma variável do escopo global (x), gerando um side effect.

```Python
# Função pura
def adicionar_cinco(x: int) -> int:
  return x + 5

x = 5
print(f"5 + 5 = {adicionar_cinco(x)}")
```

Essa função recebe um número e retorna o valor passado mais cinco, portanto é uma função pura, uma vez que não gera nenhum side effect.

## Higher order functions

Higher order functions (`hof`s) são funções que recebem uma função como parâmetro ou retornam uma função.

- HOF que retorna uma função

```Python
def hof_multiplicar(valor):
  """Função que recebe um valor e retorna uma função
  que múltiplica o parâmetro passado em primeiro lugar"""
  return lambda x: x * valor

multiplicar_por_cinco = hof_multiplicar(5)

print(f"5 x 5 = {multiplicar_por_cinco(5)}")
```

- HOF que recebe uma função

```Python
def hof_lista(lista: list, funcao):
  for elemento in lista:
    funcao(elemento)

lista = [1, 2, 3, 4, 5]
hof_lista(lista, print)
```

## Maps e filters

Maps e filters são algumas coisas trazidas da programação funcional, e que agora são encontradas em muitas linguagens de programação, mesmo que orientadas a objetos.

### Map

Para utilizarmos a função map, passamos como primeiro argumento uma função, que será executada para cada elemento e depois uma lista de elementos.

```Python
lista = [1, 2, 3]

lista_multiplicada = list(map(lambda x: x * 2, lista))

print(f"A lista original multiplicada por 2 é: {lista_multiplicada}")
```

### Filter

Utilizamos o filter para filtrar um conjunto de elementos, no exemplo a seguir filtramos apenas os números pares de uma lista.

```Python
lista = [1, 2, 3, 4]

numeros_pares = list(filter(lambda x: x % 2 == 0, lista))

print(f"Lista somente com os números pares: {numeros_pares}")
```

## Implementando as funções em um objeto

Em Python por ser uma linguagem orientada a objetos, podemos extender as funcionalidades de um objeto através do conceito de herança.

```Python
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
```

> Gostou desse Today I Learned? Deixe uma estrela para mim no repositório! 😸🌟

### Fale comigo

- [GitHub](https://github.com/Nxrth-x/)
- [LinkedIn](https://linkedin.com/in/lima-eder/)
