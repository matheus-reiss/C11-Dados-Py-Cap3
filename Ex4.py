pessoas = []


for i in range(3):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (kg): "))
    pessoas.append((nome, peso)) 


mais_pesada = pessoas[0]
mais_leve = pessoas[0]


for pessoa in pessoas:
    if pessoa[1] > mais_pesada[1]:
        mais_pesada = pessoa
    if pessoa[1] < mais_leve[1]:
        mais_leve = pessoa


print(f"\nPessoa mais pesada: {mais_pesada[0]} com {mais_pesada[1]} kg")
print(f"Pessoa mais leve: {mais_leve[0]} com {mais_leve[1]} kg")

