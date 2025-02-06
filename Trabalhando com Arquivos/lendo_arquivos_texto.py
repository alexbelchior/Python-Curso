from pathlib import Path

'''
# Lendo um arquivo de forma não recomendada
pasta_atual = Path(__file__).parent
lista_compras = open(pasta_atual / 'lista_de_compras.txt')
print(lista_compras.read())
lista_compras.close()
'''
# Lendo arquivos de forma recomendada
# A principal diferença com a forma anterior é que com o "with" você não precisa do comando close
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    print(lista_compras.read())
# Lendo linha a linha
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    linha = lista_compras.readline()
    while linha !='':
        print(linha, end='') # end tira o espaçamento entre uma linha e outra
        linha = lista_compras.readline()
print('')
print('--------------------------------------')

# Lendo todas as linhas
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    print(lista_compras.readlines())

print('--------------------------------------')

# Escrevendo arquivo
pasta_atual = Path(__file__).parent

itens_ja_comprados = ['Farinha', 'Café', 'Fermento', 'Queijo', 'Alface', 'Cenoura']

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    for item in itens_lista:
        if not item.replace('\\n', '') in itens_ja_comprados:
            lista_atualizada.write(item)

print (itens_lista)