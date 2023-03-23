lista = []
lista2 = []

for i in range(5):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
    if n % 2 == 1:
        lista2.append(n)

print(lista2)
print(sum(lista2))


