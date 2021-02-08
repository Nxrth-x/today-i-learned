def hof_multiplicar(valor: int):
    return lambda x: x * valor

multiplicar_por_10 = hof_multiplicar(10)

print(f"5 x 10 = {multiplicar_por_10(5)}")


# Por uma função ser retornada, ela pode automaticamente ser executada
# Mas o código acaba ficando bem confuso

print(f"3 x 2 = {hof_multiplicar(2)(3)}")
