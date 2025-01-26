tupla = (0, 0, 0, 1, 0, 0, 1, 0, 2, 1)

# Para encontrar a posição do elemento "2" na tupla
print(tupla.index(2))
print('---------------------------------')

# Para contar quantas vezes o elemento "0" aparece na tupla
print(tupla.count(0))
print('---------------------------------')

# Preencher uma lista vazia apenas com valores positivos
lista = [-23, -21, -13, -4, 0, 2, 5, 7, 8]

numeros_positivos = []

for numero in lista:
    if numero > 0:
        numeros_positivos.append(numero)

print('Lista original:', lista)
print(f'Lista de números positivos: {numeros_positivos}')

print('---------------------------------')

# Preencher uma lista vazia apenas com valores negativos
numeros_negativos = []
for numero in lista:
    if numero < 0:
        numeros_negativos.append(numero)
print('Lista original:', lista)
print(f'Lista de números negativos: {numeros_negativos}')
print('---------------------------------')

# Preencher uma lista com outra lista através de compreensão de listas
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_maiores_que_cinco = [numero for numero in lista1 if numero > 5]
print('Lista original:', lista1)
print(f'Lista de números maiores que cinco: {lista_maiores_que_cinco}')
print('---------------------------------')

# Inserindo um valor em uma posição específica na lista
vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')
print(vogais)
print('---------------------------------')

# Para remover um elemento da lista
vogais.remove('e')
print(vogais)
print('---------------------------------')

# Para remover o último elemento da lista
vogais.pop()
print(vogais)
print('---------------------------------') 

# Para invertar a ordem dos elementos da lista
vogais = ['a', 'e', 'i', 'o', 'u']
vogais.reverse()
print(vogais)
print('---------------------------------')

# Para ordenar os elementos da lista
vogais.sort()
print(vogais)
print('---------------------------------')

