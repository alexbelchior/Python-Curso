#Dado uma sequência de números, calcule a soma e a média dos números
#Não pode usar a função sum
print('--------------------------------------------')
valores = [10, 30, -8, 0, -2, 4]
soma = 0
for valor in valores:
    soma += valor

print(f'A soma dos valores é {soma}')
media = soma / len(valores)

print(media)

print('--------------------------------------------')
#Dado uma sequência de números, calcule o maior valor da sequência
#ATENÇÃO: Não pode usar a função max

valores = [10, 30, -8, 0, 42, 4]

maximo = valores[0]

for valor in valores:
    if valor > maximo:
        maximo = valor

print(f'O maior valor da sequência é {maximo}')

print('--------------------------------------------')
#Dado uma sequência de palavras, exiba apenas as palavras com pelo menos 7 caracteres

palavras = ['casa', 'carro', 'moto', 'bicicleta', 'caminhão', 'ônibus', 'avião']

for palavra in palavras:
    if len(palavra) >= 7:
        print(palavra)
print('--------------------------------------------')

#Dado duas listas, exiba todos os valores iguais entre as duas listas

lista1 = [1, 4, 5]
lista2 = [2, 4, 5, 6, 7]

lista3 =[]
for valor in lista1:
    for valor2 in lista2:
        if valor == valor2:
            print(f'valor {valor} aparece na duas listas')
            lista3.append(valor)
print(lista3)

#Dado duas listas, exiba uma mensagem dizendo se existe algum elemento em comum entre as duas listas
print('--------------------------------------------')

lista1 = ['Flamengo', 10, True]
lista2 = [0, False, 'Flamengo']

elemento_comum = False

for valor in lista1:
    for valor2 in lista2:
        if valor == valor2:
            elemento_comum = True
            break
print(f'Existe algum elemento em comum entre as duas listas? {elemento_comum}')