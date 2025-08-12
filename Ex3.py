aluno = {}

aluno['Nome'] = input("Digite o nome do aluno: ")
aluno['Media'] = float(input("Digite a média do aluno: "))

if aluno['Media'] >= 50:
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")