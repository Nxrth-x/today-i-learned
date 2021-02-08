import time


def benchmark(function):
    def wrapper(*args):

        start = time.perf_counter()
        result = function(*args)
        finish = time.perf_counter()

        print(f"O seu código levou {finish - start} segundos para ser executado.")

        return result
    
    return wrapper


def soma(a: int, b: int) -> int:
    return a + b


funcao_decorada = benchmark(soma)


print(f"O resultado da soma de 1 + 2 é: {funcao_decorada(1, 2)}")