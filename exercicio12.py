lista1 = []

for i in range(5):
    n1 = str(input('Adicione palavras nesta lista: '))
    lista1.append(n1)

print(lista1)

n2 = str(input('Verifique se a palavra esta na lista: '))
if n2 == n1:
    print('A palavra está na lista!')
else:
    print('A palavra não está na lista!')
