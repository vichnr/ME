def adicionar_gostos(pessoas: list, gostos: list):
    gostos_dict = {gosto['id']: gosto['gostos'] for gosto in gostos}
    
    resultado = []
    for pessoa in pessoas[:5]:
        pessoa_com_gostos = pessoa.copy()
        pessoa_id = pessoa_com_gostos['id']
        
        if pessoa_id in gostos_dict:
            pessoa_com_gostos['gostos'] = gostos_dict[pessoa_id]
        else:
            pessoa_com_gostos['gostos'] = []
        
        resultado.append(pessoa_com_gostos)
    
    return resultado

pessoas = [
    {'id': 1, 'nome': 'André', 'idade': 39},
    {'id': 2, 'nome': 'Carlos', 'idade': 45},
    {'id': 3, 'nome': 'Felipe', 'idade': 34},
    {'id': 4, 'nome': 'Lucas', 'idade': 34},
    {'id': 5, 'nome': 'Marcos', 'idade': 23}
]

gostos = [
    {"id": 1, "gostos": ['Moda', 'Ciência']},
    {"id": 2, "gostos": ['História', 'Games', 'Viagem']},
    {"id": 3, "gostos": ['Cinema', 'Natureza']},
    {"id": 4, "gostos": ['Natureza', 'Futebol']},
    {"id": 5, "gostos": ['Política', 'Dança', 'Viagem', 'Natureza']}
]

resultado = adicionar_gostos(pessoas, gostos)
print(resultado)