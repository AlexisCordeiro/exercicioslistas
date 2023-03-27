lista = []
lista2 = []

for i in range(9):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
    
lista = list(set(lista))
print(lista)
