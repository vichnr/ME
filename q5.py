def top_tres_maiores(numeros: list[int]) -> list[int]:
    numeros_ordenados = sorted(numeros, reverse=True)
    
    return numeros_ordenados[:3]


lista = [5, 42, 12, 9, 73, 51, 22]
resultado = top_tres_maiores(lista)
print(resultado)  