lista1 = []
lista2 =[]

for i in range(5):
    palavra = str(input('Escreva palavras na lista: '))
    lista1.append(palavra)
    if palavra[0] == 'a' or palavra[0] == 'A':
        lista2.append(palavra)
print(lista1)
print(lista2)