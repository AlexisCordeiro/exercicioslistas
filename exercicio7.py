lista1 = []
lista2 =[]
lista3 = []
lista = []

for i in range(4):
    palavra = str(input('Escreva palavras na lista: '))
    lista.append(palavra)
lista1 = max(lista, key = len)
lista2 = min(lista, key = len)
print(lista)
print('O maior número da lista é: ', lista1)
print('O maior número da lista é: ', lista2)







