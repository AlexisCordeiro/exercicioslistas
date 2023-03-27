lista1 = []

for i in range(5):
    n1 = int(input('Adicione números na sua lista: '))
    lista1.append(n1)

print(lista1)

lista1.sort(reverse = True)

print('O segundo número mais alto é: ', lista1[1])

