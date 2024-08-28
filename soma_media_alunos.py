alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]
print()
qnt_acima = 0
print('Alunos Acima da Média: ')
for i, nota in enumerate(notas):
    soma_media = sum(notas[i]) / 4
    if soma_media > 7:
        qnt_acima += 1
        print(alunos[i], soma_media)

print(f'A quantidade de Alunos acima da média são: {qnt_acima}')

print()
qnt_abaixo = 0
print('Alunos Abaixo da Média: ')
for i, nota in enumerate(notas):
    soma_media = sum(notas[i]) / 4
    if soma_media < 7:
        qnt_abaixo += 1
        print(alunos[i], soma_media)

print(f'A quantidade de Alunos abaixo da média são: {qnt_abaixo}')