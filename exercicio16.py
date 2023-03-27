lista = []
lista2 = []

for i in range(5):
    n = int(input('Adicione números a esta lista: '))
    lista.append(n)
    if lista.count(n)>1:
        if i not in lista2:
            lista2.append(n)
         
    
print(lista)    
print(lista2)


