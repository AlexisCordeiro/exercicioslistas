lista = []
lista2 = []

for i in range(3):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
soma = sum(lista)
elementos = len(lista)
print(soma//elementos)

