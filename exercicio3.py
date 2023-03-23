lista = []
lista2 = []

for i in range(11):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
lista.sort()
print(lista)
print('O número menor da lista é: ', lista[0])
print('o númeor maior da lista é: ', lista[-1])

