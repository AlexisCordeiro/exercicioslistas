lista = []
lista2 = []

for i in range(5):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
    
print(lista)
lista = list(set(lista))
print(lista)




