import pandas as pd

def exportar_csv(pessoas: list, nome_arquivo: str):
    df = pd.DataFrame(pessoas)
    df.to_csv(nome_arquivo, index=False)

pessoas_df = pd.read_csv('pessoas.csv')
pessoas_lista = pessoas_df.to_dict('records')

gostos_df = pd.read_csv('gostos.csv')
gostos_lista = gostos_df.to_dict('records')

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

pessoas_com_gostos = adicionar_gostos(pessoas_lista, gostos_lista)

exportar_csv(pessoas_com_gostos, "pessoas_com_gostos.csv")