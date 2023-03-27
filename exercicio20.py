lista =[]
lista2 = []

for i in range(5):
    n = str(input('Adicione palavras a sua lista: '))
    lista.append(n)
    if len(n) % 2 == 1:
        lista2.append(n)

print(lista2)


