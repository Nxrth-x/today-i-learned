# Decorators - Today I Learned 🤓

> Decorators? Parecem ser magia! 🧙‍♀️

A verdade é que não é, decorators estão presentes em muitas linguagens e são um recurso para nos ajudar com criação de funções. Decorators podem ser utilizados em muitas coisas, validação de entradas, benchmark e mais uma infinidade de casos. No exemplo abaixo iremos ver a respeito de benchmarks! ⏱

**Obs:** Irei usar `Python` para demonstrar os conceitos, mas devem se aplicar para todas linguagens que possuem suporte para decorators. 😸

## Benchmarks

### Exemplo 1 - Convencional

Você já quis testar a velocidade de alguma determinada função do seu código? Eu mesmo costumo testar o tempo de execução de uma determinada função do meu código e é sempre um trabalho enorme, principalmente quando várias funções precisam ser testadas.

É comum vermos códigos assim:

```Python
import time

def hello() -> str:
    return "Hello, world!"

start = time.perf_counter()
print(hello())
finish = time.perf_counter()

print(f"O seu código levou {finish - start} segundos para ser executado.")
```

E não tem nada de errado! Se você precisa testar seu código de maneira rápida só para conferir a performance, eu geralmente faria assim mesmo! 😺

Quer ver outra maneira de implementar isso? 🐱‍👤

### Exemplo 2 - Decorando uma função

Uma outra maneira de fazer a mesma coisa que o código acima é passando uma função para outra, efetivamente "decorando" ela. Fica mais fácil entender na prática! 👨‍💻

Primeiro definimos uma função base que irá servir para fazermos o `benchmark`.

```Python
import time

def benchmark(function):
  def wrapper(*args):
    start = time.perf_counter()
    result = function(*args)
    finish = time.perf_counter()

    print(f"O seu código levou {finish - start} segundos para ser executado.")

    return result

  return wrapper
```

> Vamos as explicações!

Primeiro definimos nossa função `benchmark`, é com ela que iremos decorar nossas funções a partir de agora. A função `benchmark` irá receber nossa função e retornará a `wrapper`.

> O que essa `wrapper` dentro da benchmark? 🤔

A `wrapper` é nossa função auxiliar, é com ela que nós faremos o calculo de tempo de execução. Note que essa função recebe `*args`, fazemos dessa forma para que possamos passar argumentos para a função interna, também.

Para utilizarmos nossa nova função, faremos dessa forma:

```Python
def soma(a: int, b: int) -> int:
  return a + b

funcao_decorada = benchmark(soma)

print(f"A soma de 1 + 2 é: {funcao_decorada(1, 2)}")
```

Simples né? Com isso agora podemos testar o tempo de execução da nossa função sem precisar escrever todo o código do `primeiro exemplo`. Sabe o que é mais legal? Isso pode ficar mais simples ainda! 🤯

### Exemplo 3 - Usando o @

O Python nos permite simplificar ainda mais a utilização de um decorator, quer ver?

```Python
@benchmark
def soma(a: int, b: int) -> int:
  return a + b

print(f"A soma de 1 + 2 é: {soma(1, 2)}")
```

Louco não? Para replicarmos o código do exemplo 2 precisamos utilizar apenas o `@benchmark` e a nossa função sai automaticamente decorada! 😸

### Conclusão

Podemos usar decorators para muitas coisas, benchmark é somente uma delas. Podemos utilizá-las para validar entradas, controlar o retorno de uma determinada função entre várias outras coisas!

> Gostou desse Today I Learned? Deixe uma estrela pra mim no repositório! 😸🌟

### Fale comigo

- [GitHub](https://github.com/Nxrth-x/)
- [LinkedIn](https://linkedin.com/in/lima-eder/)
