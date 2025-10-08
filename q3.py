pessoas = [
    {"id": 1, "nome": "André", "idade": 39},
    {"id": 2, "nome": "Carlos", "idade": 45},
    {"id": 3, "nome": "Felipe", "idade": 34},
    {"id": 4, "nome": "Lucas", "idade": 34},
    {"id": 5, "nome": "Marcos", "idade": 23},
    {"id": 6, "nome": "Fernanda", "idade": 31},
    {"id": 7, "nome": "Julia", "idade": 20}
]

gostos = [
    {"id": 1, "gostos": ["Moda", "Ciência"]},
    {"id": 2, "gostos": ["História", "Games", "Viagem"]},
    {"id": 3, "gostos": ["Cinema", "Natureza"]},
    {"id": 4, "gostos": ["Natureza", "Futebol"]},
    {"id": 5, "gostos": ["Política", "Dança", "Viagem", "Natureza"]},
    {"id": 6, "gostos": ["Leitura", "Ciência", "História", "Política", "Natureza"]},
    {"id": 7, "gostos": ["Carros"]}
]

def adicionar_gostos(pessoas: list, gostos: list) -> list:
    gostos_dict = {g['id']: g['gostos'] for g in gostos}
    resultado = []
    for pessoa in pessoas[:5]:
        pessoa_copy = pessoa.copy()
        pessoa_copy['gostos'] = gostos_dict.get(pessoa['id'], [])
        resultado.append(pessoa_copy)
    return resultado

pessoas_com_gostos = adicionar_gostos(pessoas, gostos)

import pandas as pd

def exportar_csv(pessoas: list, nome_arquivo: str):
    pessoas_formatadas = []
    for pessoa in pessoas:
        pessoa_copy = pessoa.copy()
        pessoa_copy['gostos'] = str(pessoa_copy.get('gostos', []))
        pessoas_formatadas.append(pessoa_copy)
    df = pd.DataFrame(pessoas_formatadas)
    df.to_csv(nome_arquivo, index=False)
    return df  

df = exportar_csv(pessoas_com_gostos, "pessoas.csv")

print(df)
