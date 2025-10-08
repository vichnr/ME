def criar_pessoa(nome: str, idade: int, id: int) -> dict:
    return {
        "id": id,
        "nome": nome,
        "idade": idade
    }

p1 = criar_pessoa("sakura", 12, 1)
p2 = criar_pessoa("naruto", 13, 2)
p3 = criar_pessoa("sasuke", 13, 3)

print(p1)  
print(p2)  
print(p3) 
