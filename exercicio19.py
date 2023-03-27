lista = []
lista2 = []

n2 = int(input('Digite o número dívisor: '))

for i in range(5):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
    if n % n2 == 0:
        lista2.append(n)
print('Esses são os número divisíveis pelo número que escolheu', lista2)

