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
