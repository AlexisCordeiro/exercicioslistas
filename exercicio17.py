lista =[]
lista2 = []
letra = 'e' 
letra2 = 'E'

for i in range(5):
    n = str(input('Adicione nomes a sua lista: '))
    lista.append(n)

lista2 = [x for x in lista 
          if letra or letra2 in x]

print(lista2)

