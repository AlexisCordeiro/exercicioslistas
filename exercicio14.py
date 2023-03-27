lista1 = []

for i in range(5):
    n1 = int(input('Adicione números na sua lista: '))
    lista1.append(n1)

print(lista1)

lista1.sort()

print('O segundo número mais baixo é: ', lista1[1])