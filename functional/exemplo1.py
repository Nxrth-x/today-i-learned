# Funções puras

def multiplicar_numeros(numeros: list, multiplicador: int or float) -> list:
    return [numero * multiplicador for numero in numeros]

original = [1, 2, 3]
multiplicada = multiplicar_numeros(original, 2)

print(f"A lista multiplicada é: {multiplicada}")
