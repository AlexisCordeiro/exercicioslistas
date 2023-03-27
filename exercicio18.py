lista = []
lista2 = []

for i in range(5):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
    if n % 3 == 0:
        lista2.append(n)
print(lista2)