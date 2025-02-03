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