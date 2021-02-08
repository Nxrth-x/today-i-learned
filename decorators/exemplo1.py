import time


def hello() -> str:
    return "Hello, world!"


start = time.perf_counter()
print(hello())
finish = time.perf_counter()


print(f"O seu código levou {finish - start} segundos para ser executado.")